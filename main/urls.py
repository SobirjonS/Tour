from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'tours', views.TourViewSet)


urlpatterns = [
    # Category
    path('create-category/', views.create_category, name='create-category'),
    path('get-categorys/', views.get_categorys, name='get-categorys'),
    path('update-category/<int:pk>/', views.update_category, name='update-category'),
    path('delete-category/<int:pk>/', views.delete_category, name='delete-category'),
    # Tour
    path('create-tour/', views.create_tour, name='create-tour'),
    path('', include(router.urls)),
    # path('get-tours/', views.get_tours, name='get-tours'),
    path('delete-tour/<int:pk>/', views.delete_tour, name='delete-tour'),
    path('update-tour/<int:pk>/', views.update_tour, name='update-tour'),
    # Raiting
    path('create-or-update-raiting/<int:pk>/', views.create_or_updare_raiting, name='create-or-update-raiting'),
    path('delete-raiting/<int:pk>/', views.delete_raiting, name='delete-raiting'),
    # Feedbag
    path('create-feedbag/<int:pk>/', views.create_feedbag, name='create-feedbag'),
    path('update-feedbag/<int:pk>/', views.update_feedbag, name='update-feedbag'),
    path('delete-feedbag/<int:pk>/', views.delete_feedbag, name='delete-feedbag'),
    # Booking
    path('create-booking/<int:pk>/', views.create_booking, name='create-booking')
]

urlpatterns += router.urls