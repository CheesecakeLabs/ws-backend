from django.contrib import admin
from blog import models

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['id', 'author', 'title', 'created_at']
