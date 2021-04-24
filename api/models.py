from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group, AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model


StyleTitleFormat = RegexValidator(r'^[^\s]+$', 'spaces not allowed')


class ExtendUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    receive_newsletter = models.BooleanField(default=False)
    birth_date = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=300,  blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    about_me = models.TextField(max_length=500, blank=True, null=True)
    imageUrl = models.CharField(max_length=900, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]


class Component(models.Model):
    description = models.CharField(max_length=9999999)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)


class Style(Component):
    who_can_see = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='who_can_see_style', blank=True)
    who_can_edite = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='who_can_edite_style', blank=True)
    pass


class Post(Component):
    like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_post', blank=True)
    dislike = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='dislike_post', blank=True)
    who_can_see = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='who_can_see_post', blank=True)
    who_can_edite = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='who_can_edite_post', blank=True)
    pre_build_style = models.ManyToManyField(
        Style, related_name='styles', blank=True)
    styles = models.CharField(max_length=9999999, blank=True)
    # type = ['Paper','post','template','comstume_component']
    postType = models.CharField(max_length=50, blank=True)


class Comment(Component):
    who_can_see = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='who_can_see_comment', blank=True)
    who_can_edite = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='who_can_edite_comment', blank=True)
    the_post = models.ForeignKey(
        Post, related_name='comment', on_delete=models.DO_NOTHING, null=True,)
    pass
