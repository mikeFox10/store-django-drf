from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename="hello-viewset")
router.register('profile', views.UserpProfileViewSet)

urlpatterns = [    path('hello-api-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
