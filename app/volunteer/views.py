from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, HttpResponse
from volunteer.models import Dashboards, Blogpost
from django.views.generic import View, TemplateView, ListView
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class MainView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        posts = Blogpost.objects.order_by('-id').all()
        context = {
            'posts': posts,
        }
        return context

## Education page view ##
class EduView(TemplateView):
    template_name = 'education.html'
    def get_context_data(self, **kwargs):
        pass


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = 'volunteer:login'
    template_name = 'dashboard.html'
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        boards = Dashboards.objects.order_by('-id').all()
        context = {
            'boards': boards,
        } 
        return context


class AccountView(LoginRequiredMixin, TemplateView):
    login_url = 'volunteer:login'
    template_name = 'account.html'
    def get_context_data(self, **kwargs):
        pass

@login_required
def addboard(request):
    pass

## if user exists then abort(403), fix later ##
def user_registration(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)
        return redirect('volunteer:login')
    return render(request, 'reg.html')

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

def user_logout(request):
    pass

@login_required
def shop(request):
    pass

