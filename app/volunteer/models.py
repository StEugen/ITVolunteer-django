from django.db import models
from django.db.models import JSONField
from django.contrib.auth.models import User


class Blogpost(models.Model):
    title = models.CharField(max_length=40, null=False)
    content = models.TextField(null=False)

    def __str__(self):
        return self.title

class Dashboards(models.Model):
    title = models.CharField(max_length=50, null=False)
    task = models.TextField(null=False) 
    points = models.IntegerField(null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_dashboards')
    taker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taken_dashboards', null=True)


    def __str__(self):
        return self.title

class Gids(models.Model):
    title = models.CharField(max_length=50, null=False)
    text = models.TextField(null=False)

    def __str__(self):
        return self.title
