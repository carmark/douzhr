from django.conf.urls.defaults import *
from trivias.feeds import LatestTriviasFeed

urlpatterns = patterns('',
    url(r'^$', 'trivias.views.show_latest', name='trivia-latest'),    
    url(r'^mytrivias/$', 'trivias.views.mytrivias', name='trivia-mytrivias'),
    url(r'^read/(?P<id>.+)/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'trivias.views.read_more', name='trivia-read'),
    url(r'^edit/(?P<id>.+)/$', 'trivias.views.show_edit_form', name='trivia-edit'),
    url(r'^delete/(?P<id>.+)/$', 'trivias.views.delete_trivia', name='trivia-delete'),
    url(r'^add/$', 'trivias.views.add_trivia', name='trivia-add'),
    url(r'^update/$', 'trivias.views.update_trivia', name='trivia-update'),
    url(r'^by/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'trivias.views.by_tag', name='trivia-by-tag'),
    url(r'^search/$', 'trivias.views.simple_search', name='trivia-simple-search'),
    url(r'^rate/(?P<id>.+)/$', 'trivias.views.rate_trivia', name='trivia-rate'),
    url(r'^bookmark/(?P<id>.+)/$', 'trivias.views.bookmark_trivia', name='trivia-bookmark'),
)
