from django.db import models
from django.urls import reverse
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=50, choices=(
        ('politics', 'Politics'),
        ('sports', 'Sports'),
        ('entertainment', 'Entertainment'),
        ('technology', 'Technology')
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class LinkNewsExclusive(models.Model):
    news = models.ForeignKey('news.News', on_delete=models.CASCADE)
    code_link = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.news.title

    @property
    def expirate(self):
        seconds_per_expiration = abs((self.created_at - timezone.now()).total_seconds())
        if seconds_per_expiration >= 3600:
            return True
        else:
            return False

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.news.id)])