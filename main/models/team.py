from django.db import models


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return '%s %s' % (self.id, self.name)

    class Meta:
        db_table = "team"
