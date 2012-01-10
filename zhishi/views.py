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
from zhishi.forms import ZhishiForm
from zhishi.models import Zhishi, Bookmark

        

def _show_zhishi_latest_in_home(request, zhishi=None, tag=None):
    if zhishi is None:
        zhishi = Zhishi.objects.filter(is_public=True, approved=True, is_deleted=False)
    
    if not tag is None:
        tips = TaggedItem.objects.get_by_model(tips, tag)
    
    context = {'zhishi': zhishi , 'active_menu':'home'}
    return direct_to_template(request, 'index.html', context)
    

def show_latest(request):
    return _show_zhishi_latest_in_home(request)


def by_tag(request, slug):
    try:
        tag = Tag.objects.get(slug=slug)
        return _show_zhishi_latest_in_home(request, None, tag)
    except:
        raise Http404
        

def read_more(request, id, slug=None):
    zhishi= get_object_or_404(Zhishi, pk=id)
    
    if not zhishi.author == request.user:
        zhishi.hits += 1
        zhishi.save()
    
    context = {'zhishi': zhishi, 'active_menu':'home'}
    try:
        rating = zhishi.rating_set.get(user=request.user)
        context.update({'rating': rating})
    except:
        pass
        
    try:
        bookmark = zhishi.bookmark_set.get(user=request.user)
        context.update({'bookmark': bookmark})
    except:
        pass
    
    return direct_to_template(request, 'read.html', context)


def simple_search(request):
    if 'text' in request.GET:
        text = request.GET['text']
        
        zhishi = Zhishi.objects.filter(Q(title__icontains=text) | Q(body__icontains=text))
        return _show_zhishi_latest_in_home(request, zhishi, None)
    
    return HttpResponseRedirect(reverse('zhishi-latest'))


#login_required
def myzhishi(request, form=None):
    if form == None:
        form = ZhishiForm()
    zhishi = Zhishi.objects.filter(author=request.user)
    bookmarked_zhishi = Bookmark.objects.filter(user=request.user)
    
    context = {'zhishi':zhishi, 'bookmarked_zhishi': bookmarked_zhishi, 'form': form, 'active_menu':'myzhishi'}
    return direct_to_template(request, 'myzhishi.html', context)


@login_required
def add_zhishi(request):
    if request.POST:
        form = ZhishiForm(request.POST)
        try:
            form.save()
            return HttpResponseRedirect(reverse('zhishi-myzhishi'))
        except:
            pass
            
        return myzhishi(request, form)
    #return HttpResponseRedirect(reverse('tip-mytips'))
    return direct_to_template(request, 'edit.html', {'form':ZhishiForm()})


@login_required
def delete_zhishi(request, id):
    zhishi = get_object_or_404(Zhishi, id=id, author=request.user)
    zhishi.delete_zhishi()
    zhishi.save()
    return HttpResponseRedirect(reverse('zhishi-myzhishi'))


@login_required
def show_edit_form(request, id, slug=None):
    zhishi = get_object_or_404(zhishi, id=id, author=request.user)
    context = {'form': ZhishiForm(instance=zhishi), 'active_menu':'myzhishi'}
    return direct_to_template(request, 'edit.html', context)


@login_required
def update_zhishi(request):
    if request.POST:
        id = request.POST.get('id')
        zhishi = get_object_or_404(Zhishi, id=id, author=request.user)
        form = ZhishiForm(request.POST, instance=zhishi)
        try:
            form.save()
            return HttpResponseRedirect(reverse('zhishi-myzhishi'))
        except:
            pass
            
    context = {'form':form , 'active_menu':'myzhishi'}
    return direct_to_template(request, 'edit.html', context)


@login_required
def rate_zhishi(request, id):
    if 'score' in request.GET:
        is_useful = (request.GET.get('score') == 'up')
        zhishi= get_object_or_404(Zhishi, id=id)
        
        if not request.user == zhishi.author:
            try:
                rating = zhishi.rating_set.get(user=request.user)
                rating.useful = is_useful
                rating.save()
            except:
                rating = zhishi.rating_set.create(user=request.user, useful=is_useful)
            
            try:
                if '/zhishi/read/' in request.META['HTTP_REFERER']:
                    return HttpResponseRedirect(request.META['HTTP_REFERER'])
            except:
                pass
            
    return HttpResponseRedirect(reverse('zhishi-myzhishi'))


@login_required
def bookmark_zhishi(request, id):
    if 'action' in request.GET:
        zhishi = get_object_or_404(Zhishi, pk=id)
        
        if not request.user == zhishi.author:
            action = request.GET.get('action')
            if action == 'add':
                bookmarked_zhishi = zhishi.bookmark_set.get_or_create(user=request.user)
                
            elif action == 'delete':
                try:
                    bookmarked_zhishi = zhishi.bookmark_set.get(user=request.user)
                    bookmarked_zhishi.delete_bookmark()
                    bookmarked_zhishi.save()
                except:
                    pass

            try:
                if '/zhishi/read/' in request.META['HTTP_REFERER']:
                    return HttpResponseRedirect(request.META['HTTP_REFERER'])
            except:
                pass

    return HttpResponseRedirect(reverse('zhishi-myzhishi'))
