# 31. Configure view URL
# 40. Add URL Router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-vieset', views.HelloViewSet, base_name='hello-viewset')
# 48. Register profile Viewset with the URL router
router.register('profile', views.UserProfileViewSet)  # base_name is not required when you use queryset

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('another-view/', views.AnotherApiView.as_view()),
    path('', include(router.urls))
]
