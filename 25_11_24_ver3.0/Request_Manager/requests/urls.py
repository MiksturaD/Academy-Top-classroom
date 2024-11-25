from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_list, name='request_list'),
    path('add/', views.create_request, name='create_request'),


]