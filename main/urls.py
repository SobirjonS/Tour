from django.urls import path
from . import views


urlpatterns = [
    # Category
    path('create-category/', views.create_category, name='create-category'),
    path('get-categorys/', views.get_categorys, name='get-categorys'),
    path('update-category/<int:pk>/', views.update_category, name='update-category'),
    path('delete-category/<int:pk>/', views.delete_category, name='delete-category'),
    # Tour
    path('create-tour/', views.create_tour, name='create-tour'),
    path('get-tours/', views.get_tours, name='get-tours'),
    path('delete-tour/<int:pk>/', views.delete_tour, name='delete-tour'),
    path('update-tour/<int:pk>/', views.update_tour, name='update-tour'),
    path('test_email', views.test_email)
]