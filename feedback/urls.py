from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'feedback.views.show_feedback_form', name='feedback-form'),    
)
