from django.contrib import admin
from volunteer.models import Dashboards, User, Volunteers, Blogpost

admin.site.register(User)
admin.site.register(Volunteers)
admin.site.register(Blogpost)
admin.site.register(Dashboards)
