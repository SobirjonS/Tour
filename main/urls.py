from django.urls import path
from . import views


urlpatterns = [
    # Category
    path('create-category/', views.create_category, name='create-category'),
    path('get-category/', views.get_category, name='get-category'),
    path('update-category/<int:pk>/', views.update_category, name='update-category'),
    # Tour
    path('create-tour/', views.create_tour, name='create-tour'),
    path('test_email', views.test_email)
]