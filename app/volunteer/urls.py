# urls for volunteer app
from django.urls import path
from . import views
from volunteer.views import MainView


app_name = 'volunteer'
urlpatterns = [
    path('', MainView.as_view(), name='index'),
]