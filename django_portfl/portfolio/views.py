from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import Project, UserProfile
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()
    user = UserProfile.objects.first()
    success = False

    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    'Message from portfolio site',
                    f'Name: {name}\nEmail: {email}\nMessage: {message}',
                    email,
                    ['nikolasdurango@gmail.com']
                )
                success = True
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    form = ContactForm()

    return render(request, 'home.html', {'projects': projects, 'form': form, 'user': user, 'success': success})