from django.contrib import admin
from .models import Project, Tag


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'url_demo', 'url_source']
    filter_horizontal = ('tags',)

admin.site.register(Tag)
admin.site.register(Project, ProjectAdmin)