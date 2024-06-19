from django.urls import path

from . import views

app_name = 'reg' 

urlpatterns = [
    #  path("", views.login_page, name="newuser"),
    path("logout/", views.logout_user, name="logout"),
    path("login/", views.login_user, name="login"),
    path('register/', views.inscription, name='register'),
     
]
