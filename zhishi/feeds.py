#-*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from zhishi.models import Zhishi
import datetime

class LatestZhishiFeed(Feed):
    title = "Douzhr"
    link = "/zhishi/"
    description = "Updates on changes and additions to douzhr.com."

    def items(self):
        return Zhishi.objects.filter(is_public=True, approved=True, is_deleted=False)[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body[:140]
        
    def item_author_name(self, item):
        return item.author
    
    def item_pubdate(self, item):
        # convert date to datetime format
        d =  item.pub_date
        return datetime.datetime.combine(d, datetime.time())

