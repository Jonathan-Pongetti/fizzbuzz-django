from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('fizzbuzz/', views.fizzBuzz, name="fizzbuzz"),
    path('fizzbuzz/<str:pk>', views.getFizzBuzz, name ="getFizzBuzz")
]