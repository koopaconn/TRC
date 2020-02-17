from django.contrib import auth
from django.db import models
from django.utils import timezone


class model_users(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
