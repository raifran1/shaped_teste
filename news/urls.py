from django.urls import path
from news.views import NewsAPIView, LinkNewsAPIView

urlpatterns = [
    path("link/", LinkNewsAPIView.as_view(), name="link-news-generate-api"),
    path("link/<code_link>/", LinkNewsAPIView.as_view(), name="link-news-api"),
    path("news/", NewsAPIView.as_view(), name="news-api"),
    path("news/<int:pk>/", NewsAPIView.as_view(), name="news-api-detail"),
]
