from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class UserProfile(models.Model):
    name = models.CharField(_('User Name'), max_length=80)
    email = models.EmailField('Email')
    image = models.ImageField(
        _('Profile Image'), upload_to='portfolio/images/',
    )
    cv = models.FileField(
        _('CV File'), upload_to='portfolio/files/',
    )
    linkedin = models.URLField('Linkedin', blank=True)
    github = models.URLField('Github', blank=True)

    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')

    def __str__(self):
        return self.name

class Project(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('Project Title'), max_length=150),
        description = models.CharField(_('Project Description'), max_length=254),
        image = models.ImageField(
            _('Project Image'),
            upload_to='portfolio/images/',
        ),
        tags = models.ManyToManyField('Tag'),
        url_demo = models.URLField(_('URL Demo'), blank=True),
        url_source = models.URLField(_('URL Source'), blank=True)
    )
    

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(_('Tag Name'), max_length=80)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name