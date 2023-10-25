from django.urls import reverse
from rest_framework import serializers
from news.models import News, LinkNewsExclusive

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class LinkNewsExclusiveSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    class Meta:
        model = LinkNewsExclusive
        fields = ['link']

    def get_link(self, obj):
        return reverse('link-news-api', kwargs={'code_link': obj.code_link})