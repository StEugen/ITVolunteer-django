from django.shortcuts import render
from django.http import HttpResponse
from volunteer.models import Dashboards, Volunteers, User, Blogpost
from django.views.generic import View, TemplateView, ListView


class MainView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        posts = Blogpost.objects.all()
        context = {
            'posts': posts,
        }
        return context
