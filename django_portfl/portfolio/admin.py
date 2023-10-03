from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import UserProfile, Project, Tag

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Project, TranslatableAdmin)
admin.site.register(Tag)