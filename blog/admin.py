# admin.py
from django.contrib import admin
from .models import Post
from .models import Discussion

admin.site.register(Discussion)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title']  # Replace 'title' with the actual field in your Post model

admin.site.register(Post, PostAdmin)

 


