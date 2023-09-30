from django import forms
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(label=_('Name *'), max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control no-box-shadow', 'placeholder': _('Enter your name'), 'required': True
        }))
    email = forms.EmailField(label=_('Email *'), max_length=50, widget=forms.EmailInput(attrs={
        'class': 'form-control no-box-shadow', 'placeholder': _('Enter your Email'), 'required': True
        }))
    message = forms.CharField(label=_('Message *'), widget=forms.Textarea(attrs={
        'class': 'form-control no-box-shadow', 'placeholder': _('Enter your message'), 'required': True, 'rows': 5
        }))
