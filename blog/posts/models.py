from django.db import models

from oauth.models import AuthUser


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=5000)
    author = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)


class Like_post(models.Model):
    author = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)


class Post_tag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Image(models.Model):
    image_url = models.URLField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)


class Post_image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)


