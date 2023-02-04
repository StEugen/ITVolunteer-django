from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, HttpResponse
from volunteer.models import Dashboards, Volunteers, User, Blogpost
from django.views.generic import View, TemplateView, ListView
from django.contrib.auth import authenticate,login
from django.contrib import messages


class MainView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        posts = Blogpost.objects.all()
        context = {
            'posts': posts,
        }
        return context


def user_registration(request):
    pass

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, 
                            username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('volunteer:index')
        else:
            messages.success(request, ("There was a problem"))
            return redirect('volunteer:login')
    return render(request, 'login.html')