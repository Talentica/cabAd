from django.contrib.auth.models import AbstractUser
from django.db import models
from .team import Team


class User(AbstractUser):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    office = models.CharField(max_length=255, null=False)

    def __str__(self):
        return '%s %s' % (self.id, self.username)
