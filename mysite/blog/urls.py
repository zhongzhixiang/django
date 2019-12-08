from django.urls import path

from . import views
urlpatterns = [
path('articles/', views.article),
path('post/(\d+)/', views.detail)
]
