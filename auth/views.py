from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core import mail

from decouple import config
from main import models
from . import serializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def update_password(request):
    user = request.user
    print(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    reset_url = request.build_absolute_uri(reverse('reset_password_with_token', kwargs={'uidb64': uid, 'token': token}))
    
    mail.send_mail(
        'Reset Your Password',
        f'Click the link to reset your password: {reset_url}',
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )
    return Response({"detail": "Password reset link has been sent to your email."}, status=200)


@api_view(['POST'])
def reset_password_with_token(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = models.CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, models.CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            new_password = request.data.get('new_password')
            confirm_password = request.data.get('confirm_password')

            if new_password and new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                return Response({"detail": "Password updated successfully"}, status=200)
            else:
                return Response({"detail": "Passwords do not match"}, status=400)
        return render(request, 'reset_password.html', {'validlink': True, 'uidb64': uidb64, 'token': token})
    else:
        return render(request, 'reset_password.html', {'validlink': False})
    

@api_view(['POST'])
def sign_up(request):
    username = f"{request.data.get('first_name')} {request.data.get('last_name')}"
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')
    password_confirm = request.data.get('password_confirm')  
    if models.CustomUser.objects.filter(email=email).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    else: 
        if password == password_confirm:
            user = models.CustomUser.objects.create_user(
                                                          username=username,
                                                          first_name=first_name, 
                                                          last_name=last_name,
                                                          email=email,
                                                          phone_number=phone_number,
                                                          password=password,
                                                          )
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
 

@api_view(['POST'])
def sign_in(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    print(user)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def update_user_data(request):    
    serializer = serializers.CustomUserSerializer(request.user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def sign_out(request):
    request.user.auth_token.delete()
    return Response({'message': 'Successfully signed out'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_user_data(request):
    serializer = serializers.CustomUserSerializer(request.user)
    return Response(serializer.data)