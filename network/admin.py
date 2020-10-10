from django.contrib import admin
from .models import User, Followers, Post


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email")


class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "content")


class FollowersAdmin(admin.ModelAdmin):
    list_display = ("user", "follower")


admin.site.register(User, UserAdmin)
admin.site.register(Followers, FollowersAdmin)
admin.site.register(Post, PostAdmin)
