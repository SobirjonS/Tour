from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from django.db import transaction

from . import models
from . import serialisers

from django.core.mail import send_mail
from decouple import config

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def test_email(request):
    user = request.user
    send_mail('Subject here','keldi',config('EMAIL_HOST_USER'),[user.email],fail_silently=False,)


# Category
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_category(request):
    try:
        name = request.data['name']
        models.Category.objects.create(
            name=name
        )
        return Response("The category has been created", status.HTTP_200_OK)
    except:
        return Response('Bad request', status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_category(request):
    categorys = models.Category.objects.all()
    serialiser = serialisers.CategorySerializer(categorys, many=True)
    return Response(serialiser.data, status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def update_category(request, pk):
    try:
        category = models.Category.objects.get(pk=pk)
        category.name = request.data['name']
        category.save()
        return Response("The category has been changed", status.HTTP_200_OK)
    except:
        return Response('Bad request', status.HTTP_400_BAD_REQUEST)


# Tour
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_tour(request):
    user = request.user
    data = request.data
    try:
        images = request.FILES.getlist('image')
        videos = request.FILES.getlist('media')
        service = data['service_description']

        tour = models.Tour.objects.create(
            owner=user,
            name=data['name'],
            description=data['description'],
            cost=data['cost'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            seats=data['seats']
        )

        for image in images:
            models.TourImage.objects.create(
                image=image,
                tour=tour
            )

        for media in videos:
            models.TourVideo.objects.create(
                media=media,
                tour=tour
            )
        
        models.TourService.objects.create(
            service_description=service,
            tour=tour
        )
        return Response('Complated !', status.HTTP_200_OK)
    except:
        return Response('Bad request', status.HTTP_400_BAD_REQUEST)
