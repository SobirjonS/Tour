from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('get-user-data/', views.get_user_data, name='get-user-data'),
    path('update-user-data/', views.update_user_data, name='update-user-data'),
        path('update_password/', views.update_password, name='update_password'),
    path('reset_password/<uidb64>/<token>/', views.reset_password_with_token, name='reset_password_with_token'),
]