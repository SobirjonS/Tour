from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from main import models
from . import serializers

from django.contrib.auth import authenticate


@api_view(['POST'])
def sign_up(request):
    username = request.data.get('first_name')
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
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
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


@api_view(['POST'])
def request_password_reset(request):
    email = request.data.get('email')
    try:
        user = models.CustomUser.objects.get(email=email)
    except models.CustomUser.DoesNotExist:
        return Response({'error': 'User with this email does not exist'}, status=status.HTTP_404_NOT_FOUND)

    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    reset_url = f"http://yourfrontend.com/reset_password_confirm/{uid}/{token}/"
    message = render_to_string('password_reset_email.html', {'reset_url': reset_url})
    
    send_mail(
        'Password Reset Request',
        message,
        'iamkirito016002@gmail.com',
        [email],
        fail_silently=False,
    )
    
    return Response({'message': 'Password reset email has been sent'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def reset_password_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = models.CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, models.CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        new_password = request.data.get('new_password')
        new_password_confirm = request.data.get('new_password_confirm')

        if new_password != new_password_confirm:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()
        return Response({'message': 'Password has been reset'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid token or user'}, status=status.HTTP_400_BAD_REQUEST)
