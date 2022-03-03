from django.contrib import admin

from .models import Diary


class DiariesAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['title', 'id']


admin.site.register(Diary, DiariesAdmin)
