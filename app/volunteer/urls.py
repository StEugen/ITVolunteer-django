# urls for volunteer app
from django.urls import path
from . import views
from volunteer.views import MainView, DashboardView, EduView, AccountView


app_name = 'volunteer'
urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('registration', views.user_registration, name='registration'),
    path('login', views.user_login, name='login'),
    path('dashboards', DashboardView.as_view(), name='dashboards'),
    path('dashboards/addboard', views.addboard, name='addboard'),
    path('dashboards/addboardform', views.board_adding_page, name='addboardform'),
    path('dashboards/takeboard', views.take_board, name='takeboard'),
    path('education', EduView.as_view(), name='education'),
    path('account', AccountView.as_view(), name='account'),
]