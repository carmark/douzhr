# -*- coding: utf-8 -*-
from django.contrib.admin import site, ModelAdmin
from django.contrib.sitemaps import ping_google
from django.conf import settings
from django.core.mail import EmailMessage

from zhishi.models import Zhishi, Rating, Bookmark, Category
from zhishi.forms import ZhishiForm

class ZhishiAdmin(ModelAdmin):
    search_fields = ('title', 'body')
    list_display = ('title', 'id', 'author', 'pub_date', 'hits', 'enable_comments', 'is_public', 'approved')
    list_filter = ('author', 'enable_comments', 'is_public', 'approved')
    list_per_page = 20
    date_hierarchy = 'pub_date'
    ordering = ('-id', '-pub_date')
    actions = ['approve', 'reject', 'post_twitter']

    def _notificate_user_about_rejection_for(self, zhishi):
        
        message_pt_br = u"""\
        Desculpe.
        
        A dica %s foi rejeitada no site tipsforlinux.com.
        Há 2 possíveis motivos para isso:

        1. A dica talvez tenha sido duplicada ou há outro dica muito parecida.
        2. A dica é inapropriada. O assunto não tem relação com o tipo de conteúdo do site.

        Agradecemos pela compreensão!
        """ % zhishi.title

        message_en_us = u"""\
        Sorry.

        The tip %s has been rejected on tipsforlinux.com.
        There are two possible reasons for this:

        1. The tip was maybe duplicated or there is another tip very similar.
        2. The tip is inappropriate. The subject is not on the contents of the site.

        Thank you for understanding!
        """ % zhishi.title

        subject = 'Your tip has been rejected on tipsforlinux.com website'
        message = "%s\n\n----------------------------\n\n\n%s" % (message_pt_br, message_en_us)
        mail = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [tip.author.email, ])
        mail.send()
        
    def approve(self, request, queryset):
        queryset.update(approved=True)
        try:
            ping_google()
        except Exception:
            pass
    approve.short_description = 'Approve'

    def reject(self, request, queryset):
        queryset.update(approved=False)
        first_tip = [ tip for zhishi in queryset ][0]
        try:
            self._notificate_user_about_rejection_for(first_tip)
            ping_google()
        except Exception:
            pass
    reject.short_description = 'Reject'
    
site.register(Zhishi, ZhishiAdmin)

class RatingAdmin(ModelAdmin):
    list_display = ('id', 'zhishi', 'user', 'useful')
site.register(Rating, RatingAdmin)

site.register(Bookmark)
site.register(Category)
