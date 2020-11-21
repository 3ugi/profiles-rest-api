# 31. Configure view URL
from django.urls import path

from profiles_api import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('another-view/', views.AnotherApiView.as_view())
]