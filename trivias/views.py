# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template
from django.contrib.comments.views.comments import post_comment
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import Http404

from tagging.models import Tag, TaggedItem
from trivias.forms import TriviaForm
from trivias.models import Trivia, Bookmark

        

def _show_trivias_latest_in_home(request, trivias=None, tag=None):
    if trivias is None:
        trivias = Trivia.objects.filter(is_public=True, approved=True, is_deleted=False)
    
    if not tag is None:
        trivias = TaggedItem.objects.get_by_model(trivias, tag)
    
    context = {'trivias': trivias, 'active_menu':'home'}
    return direct_to_template(request, 'index.html', context)
    

def show_latest(request):
    return _show_trivias_latest_in_home(request)


def by_tag(request, slug):
    try:
        tag = Tag.objects.get(slug=slug)
        return _show_trivias_latest_in_home(request, None, tag)
    except:
        raise Http404
        

def read_more(request, id, slug=None):
    trivia = get_object_or_404(Trivia, pk=id)
    
    if not trivia.author == request.user:
        trivia.hits += 1
        trivia.save()
    
    context = {'trivia': trivia, 'active_menu':'home'}
    try:
        rating = trivia.rating_set.get(user=request.user)
        context.update({'rating': rating})
    except:
        pass
        
    try:
        bookmark = trivia.bookmark_set.get(user=request.user)
        context.update({'bookmark': bookmark})
    except:
        pass
    
    return direct_to_template(request, 'read.html', context)


def simple_search(request):
    if 'text' in request.GET:
        text = request.GET['text']
        
        trivias = Trivia.objects.filter(Q(title__icontains=text) | Q(body__icontains=text))
        return _show_trivias_latest_in_home(request, trivias, None)
    
    return HttpResponseRedirect(reverse('trivia-latest'))


@login_required
def mytrivias(request, form=None):
    if form == None:
        form = TriviaForm()
    trivias = Trivia.objects.filter(author=request.user)
    bookmarked_trivias = Bookmark.objects.filter(user=request.user)
    
    context = {'trivias':trivias, 'bookmarked_trivias': bookmarked_trivias, 'form': form, 'active_menu':'myzhishi'}
    return direct_to_template(request, 'mytrivias.html', context)


@login_required
def add_trivia(request):
    if request.POST:
        form = TriviaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('trivia-mytrivias'))

    return direct_to_template(request, 'add.html', {'form':TriviaForm()})


@login_required
def delete_trivia(request, id):
    trivia = get_object_or_404(Trivia, id=id, author=request.user)
    trivia.deletetrivia()
    trivia.save()
    return HttpResponseRedirect(reverse('trivia-mytrivias'))


@login_required
def show_edit_form(request, id, slug=None):
    trivia = get_object_or_404(Trivia, id=id, author=request.user)
    context = {'form': ZhishiForm(instance=trivia ), 'active_menu':'myzhishi'}
    return direct_to_template(request, 'edit.html', context)


@login_required
def update_trivia(request):
    if request.POST:
        id = request.POST.get('id')
        trivia = get_object_or_404(Trivia, id=id, author=request.user)
        form = TriviaForm(request.POST, instance=trivia)
        try:
            form.save()
            return HttpResponseRedirect(reverse('trivia-mytrivias'))
        except:
            pass
            
    context = {'form':form , 'active_menu':'myzhishi'}
    return direct_to_template(request, 'edit.html', context)


@login_required
def rate_trivia(request, id):
    if 'score' in request.GET:
        is_useful = (request.GET.get('score') == 'up')
        trivia = get_object_or_404(Trivia, id=id)
        
        if not request.user == trivia.author:
            try:
                rating = trivia.rating_set.get(user=request.user)
                rating.useful = is_useful
                rating.save()
            except:
                rating = trivia.rating_set.create(user=request.user, useful=is_useful)
            
            try:
                if '/read/' in request.META['HTTP_REFERER']:
                    return HttpResponseRedirect(request.META['HTTP_REFERER'])
            except:
                pass
            
    return HttpResponseRedirect(reverse('trivia-mytrivias'))


@login_required
def bookmark_trivia(request, id):
    if 'action' in request.GET:
        trivia = get_object_or_404(Trivia, pk=id)
        
        if not request.user == trivia.author:
            action = request.GET.get('action')
            if action == 'add':
                bookmarked_trivia = trivia.bookmark_set.get_or_create(user=request.user)
                
            elif action == 'delete':
                try:
                    bookmarked_trivia = trivia.bookmark_set.get(user=request.user)
                    bookmarked_trivia.delete_bookmark()
                    bookmarked_trivia.save()
                except:
                    pass

            try:
                if '/read/' in request.META['HTTP_REFERER']:
                    return HttpResponseRedirect(request.META['HTTP_REFERER'])
            except:
                pass

    return HttpResponseRedirect(reverse('trivia-mytrivias'))
