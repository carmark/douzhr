#-*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from zhishi.models import Zhishi 
import datetime

class LatestZhishiSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Zhishi.objects.filter(is_public=True, approved=True, is_deleted=False)

    def lastmod(self, obj):
        # convert date to datetime format
        d =  obj.pub_date
        return datetime.datetime.combine(d, datetime.time())
