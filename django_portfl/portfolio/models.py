from django.db import models


class Project(models.Model):
    title = models.CharField('Project Title', max_length=150)
    description = models.CharField('Project Description', max_length=254)
    image = models.ImageField(
        'Project Image',
        upload_to='portfolio/images/',
    )
    tags = models.ManyToManyField('Tag')
    url_demo = models.URLField('Url Demo', blank=True)
    url_source = models.URLField('Url Source', blank=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField('Tag Name', max_length=80)

    class Meta:
        verbose_name = ('Tag')
        verbose_name_plural = ('Tags')

    def __str__(self):
        return self.name