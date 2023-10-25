from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from news.models import News, LinkNewsExclusive
from news.serializers import NewsSerializer, LinkNewsExclusiveSerializer
from news.utils import get_code


class NewsAPIView(APIView, PageNumberPagination):
    permission_classes = []
    authentication_classes = []

    def get(self, request, pk=None) -> Response:
        if pk:
            news = News.objects.get(pk=pk)
            serializer = NewsSerializer(news, many=False)
            return Response(serializer.data)
        else:
            news = News.objects.all()

            # logica da paginação -> retorna um page obj
            news_paginate = self.paginate_queryset(news, request)

            serializer = NewsSerializer(news_paginate, many=True)

            # retorno deve ser exclusivo para retornar os parâmetros count, next, previous e results.
            return self.get_paginated_response(serializer.data)

    def post(self, request) -> Response:
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            news_article = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = NewsSerializer(news_article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            news_article = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        news_article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LinkNewsAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, code_link=None) -> Response:
        if code_link:
            try:
                link_news_exclusive = LinkNewsExclusive.objects.get(code_link=code_link)
                if link_news_exclusive.expirate:
                    return Response({'detail': 'Link expirado'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    serializer = NewsSerializer(link_news_exclusive.news, many=False)
                    return Response(serializer.data)
            except LinkNewsExclusive.DoesNotExist:
                return Response({'detail': 'Link inexistente'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request) -> Response:
        try:
            news = News.objects.get(pk=request.data.get('news_pk'))
            code_link = get_code(25)
            link_exlusive = LinkNewsExclusive.objects.create(
                news=news,
                code_link=code_link
            )
            serializer = LinkNewsExclusiveSerializer(link_exlusive)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except News.DoesNotExist:
            return Response({'detail': 'Notícia não encontrada'}, status=status.HTTP_404_NOT_FOUND)

