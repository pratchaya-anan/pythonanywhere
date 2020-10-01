from django.urls import path

from . import views

urlpatterns = [
    # ex: /myweb/
    path('', views.index, name='index'),
]