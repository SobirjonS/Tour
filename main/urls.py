from django.urls import path
from . import views


urlpatterns = [
    path('tours-create/', views.create_tour, name='create-tour'),
]