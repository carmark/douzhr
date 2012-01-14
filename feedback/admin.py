from django.contrib.admin import site, ModelAdmin
from feedback.models import Feedback 

site.register(Feedback)
