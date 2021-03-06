from django.conf.urls.defaults import patterns, include, url
from trivias.sitemaps import LatestTriviasSitemap

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'trivias': LatestTriviasSitemap}}),
    url(r'robots\.txt$', include('robots.urls')),
#    url(r'^$', 'zhishi.views.show_latest'),
#    url(r'^zhishi/', include('zhishi.urls')),
    url(r'^$', 'trivias.views.show_latest'),
    url(r'^trivias/', include('trivias.urls')),
    url(r'^feedback/', include('feedback.urls')),
)


from django.conf import settings
if settings.LOCAL:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    )
