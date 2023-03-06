from email.policy import default

from django.db import models

from oauth.models import AuthUser
from posts.models import Post


class Comment(models.Model):
    text = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    comment_to_comment = models.ForeignKey('self', on_delete=models.CASCADE, default=None)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)


class Like_comment(models.Model):
    author = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)
