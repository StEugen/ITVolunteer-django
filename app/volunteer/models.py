from django.db import models
from django.db.models import JSONField
from django.contrib.auth.models import User #Group, Permission
#from django.contrib.contenttypes.models import ContentType


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


#take_dashboard_permission, created = Permission.objects.get_or_create(
#    codename='take_dashboard',
#    name='Can take a dashboard',
#    content_type_id=ContentType.objects.get_for_model(Dashboards).id
#)

#complete_dashboard_permission, created = Permission.objects.get_or_create(
#    codename='complete_dashboard',
#    name='Can complete a dashboard',
#    content_type_id=ContentType.objects.get_for_model(Dashboards).id
#)

#volunteers_group, created = Group.objects.get_or_create(name='volunteers')
#volunteers_group.permissions.add(take_dashboard_permission)
#volunteers_group.permissions.add(complete_dashboard_permission)