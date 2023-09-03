from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name *", max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control no-box-shadow', 'placeholder': 'Enter your name', 'required': True
        }))
    email = forms.EmailField(label="Email *", max_length=50, widget=forms.EmailInput(attrs={
        'class': 'form-control no-box-shadow', 'placeholder': 'Enter your Email', 'required': True
        }))
    message = forms.CharField(label="Message *", widget=forms.Textarea(attrs={
        'class': 'form-control no-box-shadow', 'placeholder': 'Enter your message', 'required': True, 'rows': 5
        }))
