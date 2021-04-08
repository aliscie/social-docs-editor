import graphene
from graphene_django import DjangoObjectType
from . import models
from django.conf import settings


class Users(DjangoObjectType):
    class Meta:
        model = models.ExtendUser
        fields = "__all__"


class Posts(DjangoObjectType):
    class Meta:
        model = models.Post
        fields = "__all__"


class Style(DjangoObjectType):
    class Meta:
        model = models.Comment
        fields = "__all__"