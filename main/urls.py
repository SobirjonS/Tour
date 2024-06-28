from django.urls import path, include
from rest_framework.routers import DefaultRouter

from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'tours', views.TourViewSet)

router.register(r'booking', views.BookingViewSet)


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
    path('create-booking/<int:pk>/', views.create_booking, name='create-booking'),
    path('update-booking/<int:pk>/', views.update_booking, name='update-booking'),
    path('get-booking/', views.get_booking, name='get-booking'),
    path('', include(router.urls)),
    #
    path('get-bookings-by-day/<int:year>/<int:month>/<int:day>/', views.get_bookings_by_day, name='get-bookings-by-day'),
    path('get-bookings-by-week/<int:year>/<int:week>/', views.get_bookings_by_week, name='get-bookings-by-week'),
    path('get-bookings-by-month/<int:year>/<int:month>/', views.get_bookings_by_month, name='get-bookings-by-month'),
    #
    path('bookings-report-by-day/<int:year>/<int:month>/<int:day>/', views.booking_report_by_day, name='bookings-report-by-day'),
    path('bookings-report-by-week/<int:year>/<int:week>/', views.bookings_report_by_week, name='bookings-report-by-week'),
    path('bookings-report-by-month/<int:year>/<int:month>/', views.booking_report_by_month, name='bookings-report-by-month'),
    # Answer
    path('create-answer/<int:pk>/', views.create_answer, name='create-answer'),
    path('update-answer/<int:pk>/', views.update_answer, name='update-answer'),
    path('delete-answer/<int:pk>/', views.delete_answer, name='delete-answer'),
]

urlpatterns += router.urls