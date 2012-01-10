from django.conf.urls.defaults import *
from zhishi.feeds import LatestZhishiFeed

urlpatterns = patterns('',
    url(r'^$', 'zhishi.views.show_latest', name='zhishi-latest'),    
    url(r'^myzhishi/$', 'zhishi.views.myzhishi', name='zhishi-myzhishi'),
    url(r'^read/(?P<id>.+)/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'zhishi.views.read_more', name='zhishi-read'),
    url(r'^edit/(?P<id>.+)/$', 'zhishi.views.show_edit_form', name='zhishi-edit'),
    url(r'^delete/(?P<id>.+)/$', 'zhishi.views.delete_zhishi', name='zhishi-delete'),
    url(r'^add/$', 'zhishi.views.add_zhishi', name='zhishi-add'),
    url(r'^update/$', 'zhishi.views.update_zhishi', name='zhishi-update'),
    url(r'^by/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'zhishi.views.by_tag', name='zhishi-by-tag'),
    url(r'^search/$', 'zhishi.views.simple_search', name='zhishi-simple-search'),
    url(r'^rate/(?P<id>.+)/$', 'zhishi.views.rate_zhishi', name='zhishi-rate'),
    url(r'^bookmark/(?P<id>.+)/$', 'zhishi.views.bookmark_zhishi', name='zhishi-bookmark'),
)
