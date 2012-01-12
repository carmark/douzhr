#-*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from trivias.models import Trivia 
import datetime

class LatestTriviasSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Trivia.objects.filter(is_public=True, approved=True, is_deleted=False)

    def lastmod(self, obj):
        # convert date to datetime format
        d =  obj.pub_date
        return datetime.datetime.combine(d, datetime.time())
