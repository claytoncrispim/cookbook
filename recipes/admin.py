from django.contrib import admin

from . import models

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')

admin.site.register(models.Recipe, RecipeAdmin)
