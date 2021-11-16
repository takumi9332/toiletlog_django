from django.contrib import admin
from . import models


@admin.register(models.Toilet)
class ToiletAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
