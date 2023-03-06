from django.db import models

from django.core.validators import FileExtensionValidator
from base_servises.Servises import get_path_upload_avatar


class UserRole(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AuthUser(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.IntegerField()
    time_created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=get_path_upload_avatar, blank=True, null=True,
                               validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    password = models.CharField(max_length=20, default='')

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.first_name + " " + self.last_name


class Follower(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='owner')
    subscriber = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='subscriber')

    def __str__(self):
        return self.subscriber + ' follow to ' + self.user
