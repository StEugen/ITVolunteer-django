from django.db import models
from django.db.models import JSONField


class Blogpost(models.Model):
    title = models.CharField(max_length=40, null=False)
    content = models.TextField(null=False)

    def __str__(self):
        return self.title

class Dashboards(models.Model):
    title = models.CharField(max_length=50, null=False)
    points = models.IntegerField(null=False)
    author = models.ForeignKey('volunteer.User',
                                null=False, on_delete=models.DO_NOTHING,
                                related_name='Dashboards')
    volunteer = models.ForeignKey('volunteer.Volunteers',
                                    null=False, on_delete=models.DO_NOTHING,
                                    related_name='Dashboards')

    def __str__(self):
        return self.title


