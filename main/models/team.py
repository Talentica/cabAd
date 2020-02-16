from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = "team"
