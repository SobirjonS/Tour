from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from django.db import transaction

from . import models
from . import serializers

from django.core.mail import send_mail
from decouple import config

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def test_email(request):
    user = request.user
    send_mail('Subject here','keldi',config('EMAIL_HOST_USER'),[user.email],fail_silently=False,)


@api_view(['POST'])
@transaction.atomic
def create_tour(request):
    user = request.user
    if user.is_admin and user.is_partner:
        serializer = serializers.TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        Response({'message': 'You don`t have access'}, status=status.HTTP_400_BAD_REQUEST)