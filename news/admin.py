from django.contrib import admin
from news.models import News, LinkNewsExclusive

admin.site.register(News)
admin.site.register(LinkNewsExclusive)