from django.urls import path

from . import views

urlpatterns = [
    path('', views.post, name='post'),
    path('detail/<int:post_id>/', views.detail, name='detail')
]