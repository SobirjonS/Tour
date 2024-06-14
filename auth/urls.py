from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('update-user-data/', views.update_user_data, name='update-user-data'),
    path('request_password_reset/', views.request_password_reset, name='request_password_reset'),
    path('reset_password_confirm/<uidb64>/<token>/', views.reset_password_confirm, name='reset_password_confirm'),
]