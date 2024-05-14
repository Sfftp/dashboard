import sys

import django.contrib.auth.models
from django.db import models
from django.utils.translation import pgettext_lazy


__all__ = ("User",)


class UserManager(django.contrib.auth.models.UserManager):
    def get_queryset(self):
        return super().get_queryset().select_related("account")


class Account(models.Model):
    user = models.OneToOneField(
        django.contrib.auth.models.User,
        related_name="account",
        on_delete=models.CASCADE,
    )

    parameter = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.username


class User(django.contrib.auth.models.User):
    class Meta:
        proxy = True

    def add_notification(self, title, content):
        Notification.objects.create(
            user=self,
            title=title,
            content=content,
        )

    objects = UserManager()
