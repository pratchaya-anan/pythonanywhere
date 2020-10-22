"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myweb import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('login', views.login, name='login'),
    path('login_active', views.login_active, name='login'),
    path('logout', views.logout_active, name='logout'),
    path('signup',views.signup, name='sign'),
    path('signup_active', views.signup_active, name='sign'),
    path('landscape', views.landscape, name='landscape'),
    path('portrait', views.portrait, name='portrait'),
    path('food', views.food, name='food'),
]
