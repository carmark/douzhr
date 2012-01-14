# Create your views here.
from feedback.models import Feedback
from feedback.forms import FeedbackForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

def show_feedback_form(request):
    if request.POST:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('success_post.html')

    else:
        form = FeedbackForm()

    context = RequestContext(request)
    context.update({'active_menu':'feedback'})
    return render_to_response('submit_feedback.html', {'form':form}, context_instance=context)
