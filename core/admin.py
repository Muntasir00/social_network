from django.contrib import admin
from .models import Profile, Post, LikePost, CommentPost, FollowersCount

# Model Registration
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(CommentPost)
admin.site.register(FollowersCount)
