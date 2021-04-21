from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'chat'

router = DefaultRouter()

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]

urlpatterns += router.urls
