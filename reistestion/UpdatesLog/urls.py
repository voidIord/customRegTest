from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_home, name='log_home'),
    path('create', views.create, name='create'),
]
