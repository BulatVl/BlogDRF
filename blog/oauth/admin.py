from django.contrib import admin
from . import models


@admin.register(models.AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'display_name', 'time_created', )
    list_display_links = ('email',)
