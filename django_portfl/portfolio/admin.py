from django.contrib import admin
from .models import UserProfile, Project, Tag

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    filter_horizontal = ('tags',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)