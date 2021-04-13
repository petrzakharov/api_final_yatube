from django.contrib import admin

from .models import Post, Comment, Follow, Group

admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Comment)
admin.site.register(Group)
