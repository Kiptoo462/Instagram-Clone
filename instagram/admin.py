from django.contrib import admin

# Register your models here.

from .models import Profile,Post,Following,Comment

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Following)
admin.site.register(Comment)
