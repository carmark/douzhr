from django import forms
from feedback.models import Feedback

attrs_dict = {'class':'required'}
class FeedbackForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), label=u'Name')
    subject = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), label=u'Subject')
    contact = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), label=u'Contact')
    email = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), label=u'Email')
    qq_msn = forms.CharField(widget=forms.TextInput(attrs=attrs_dict), label=u'QQ/MSN')
    content = forms.CharField(widget=forms.Textarea(attrs=attrs_dict), label=u'Message')

    class Meta:
        model=Feedback 


    def save(self, *args , **kwargs):
        super(FeedbackForm, self).save(*args, **kwargs)
        
