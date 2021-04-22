from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoFormMutation
from graphene_django.utils import camelize
from graphene import relay
from django.db.models import Q
# from graphene_django.filter import DjangoFilterConnectionField
# import django_filters

import graphql_social_auth

from django import forms
from . import models
from . import schema

from graphql import GraphQLError


class Create(graphene.Mutation):
    # Reusable create function
    class Arguments:
        description = graphene.String(required=True)
    post = graphene.Field(schema.Posts)

    @classmethod
    def mutate(cls, root, info, description, *args, **kwargs):
        post = models.Post(description=description, added_by=info.context.user)
        post.save(*args, **kwargs)
        return CreatePost(post=post)
        if (not info.context.user):
            raise GraphQLError(
                "you must login to be able to create a post")


class CreatePost(Create):
    pass


class CreateStyle(Create):
    model = models.Comment
    pass


class UpdatePost(graphene.Mutation):
    # owner(added_by)+admin can update and delete
    class Arguments:
        id = graphene.Int(required=True)
        description = graphene.String()
    post = graphene.Field(schema.Posts)

    @classmethod
    def mutate(cls, root, info, id, description):
        print({"______ USER _______ update posts": info.context.user})

        post = models.Post.objects.get(id=id)
        if ((info.context.user == post.added_by) or (info.context.user.id == 1) or (info.context.user in post.who_can_edite.all())):
            post.description = description
            post.save()
            return UpdatePost(post=post)
        else:
            raise GraphQLError(
                "Only the owner of the post and the admin(website's owner) can edit and delete this post")


class UpdateUser(graphene.Mutation):
    # owner(added_by)+admin can update and delete
    class Arguments:
        username = graphene.String(required=True)
        username = graphene.String(required=False)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        is_active = graphene.String(required=False)
        # is_staff = graphene.String(required=False)
        # is_superuser = graphene.String(required=False)
        receive_newsletter = graphene.String(required=False)
        birth_date = graphene.String(required=False)
        address = graphene.String(required=False)
        city = graphene.String(required=False)
        about_me = graphene.String(required=False)

    user = graphene.Field(schema.Users)

    @classmethod
    def mutate(cls, root, info, username, *args, **kwargs):
        user = models.ExtendUser.objects.get(username=username)
        if ((info.context.user.id == 1) or (info.context.user == user)):
            for key in kwargs.keys():
                setattr(user, key, kwargs[key])
            user.save()
            return UpdateUser(user=user)
        else:
            raise GraphQLError(
                "Only "+user.username + " and the admin(website's owner) can edit and delete this profile")


class DeletePost(graphene.Mutation):
    # owner(added_by)+admin can update and delete
    class Arguments:
        id = graphene.Int(required=True)
    post = graphene.Field(schema.Posts)

    @classmethod
    def mutate(cls, root, info, id):

        get_post = models.Post.objects.get(id=id)
        post_owner = get_post.added_by
        post = models.Post.objects.get(id=id)
        if (info.context.user == post.added_by or post_owner.id == 1):
            post.delete()
            return DeletePost(post=get_post)
        else:
            raise GraphQLError(
                "Only the owner of the post ("+post_owner.username+") and the admin(website's owner) can edit or delete this post")


class Query(graphene.ObjectType):

    posts_type = graphene.List(schema.Posts, postType=graphene.String())

    def resolve_posts_type(root, info, postType):
        if (info.context.user.id == 1):
            return models.Post.objects.filter(postType=postType)
        else:
            return models.Post.objects.filter(Q(postType=postType) &
                                              (Q(who_can_see=None) or Q(who_can_see=info.context.user.id) or Q(added_by=info.context.user.id)))

    posts = graphene.List(schema.Posts)

    def resolve_posts(root, info):
        if (info.context.user.id == 1):
            return models.Post.objects.all()
        else:
            return models.Post.objects.filter(
                Q(who_can_see=None) | Q(who_can_see=info.context.user.id) | Q(added_by=info.context.user.id))

    styles = graphene.List(schema.Style)

    def resolve_styles(root, info):
        if (info.context.user.id == 1):
            return models.Style.objects.all()
        return models.Style.objects.filter(
            Q(who_can_see=None) | Q(who_can_see=info.context.user.id) | Q(added_by=info.context.user.id))

    users = graphene.List(schema.Users)

    def resolve_users(root, info):
        return models.ExtendUser.objects.all()

    user = graphene.Field(schema.Users, username=graphene.String())

    def resolve_user(root, info, username):
        return models.ExtendUser.objects.get(username=username)
        # TODO create a profile settings where users can diside wihich field to show
        # TODO
        #  @permission_check_my_field TODO create premisions function
        # if user.id ==1 return schema.Users fields ='__all__'
        # else fields ='__all__' ['username', 'id', 'imageUrl']


class Mutation(graphene.ObjectType):
    social_auth = graphql_social_auth.SocialAuthJWT.Field()
    create_post = CreatePost.Field()
    # create_style = UpdatePost.Field()
    update_post = UpdatePost.Field()
    update_user = UpdateUser.Field()
    # update_stule =
    delete_post = DeletePost.Field()
    # delete_style =


schema = graphene.Schema(query=Query, mutation=Mutation)
