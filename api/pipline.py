from .models import ExtendUser
import inspect


def save_profile(backend, user, response, *args, **kwargs):
    newuser = ExtendUser.objects.get(id=user.id)
    newuser.imageUrl = response['picture']
    newuser.save()
