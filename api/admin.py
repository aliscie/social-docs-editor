from django.contrib import admin
from . import models
import inspect

admin.site.register(models.ExtendUser)
admin.site.register(models.Comment)
admin.site.register(models.Post)
admin.site.register(models.Style)
