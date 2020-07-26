from django.urls import path, include
from . import views
from rest_framework import routers

training_router = routers.DefaultRouter()
training_router.register('schedule', views.ScheduleViewSet, basename='schedule')
app_name = 'schedule'

urlpatterns = [
    path('', include(training_router.urls))
]