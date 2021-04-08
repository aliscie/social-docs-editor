from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
# from django.conf.urls import url

from .views import schema

urlpatterns = [
      path("", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]