import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

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
def get_categorys(request):
    categorys = models.Category.objects.all()
    serialiser = serializers.CategorySerializer(categorys, many=True)
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
        return Response('Did not find such information', status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def delete_category(request, pk):
    try:
        category = models.Category.objects.get(pk=pk)
        category.delete()
        return Response("The category has been deleted", status.HTTP_200_OK)
    except:
        return Response('Did not find such information', status.HTTP_400_BAD_REQUEST)


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
        services = request.POST.getlist('service')
        category = models.Category.objects.get(id=data['category'])

        tour = models.Tour.objects.create(
            creator=user,
            category=category,
            place_name=data['place_name'],
            title=data['title'],
            body=data['body'],
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
            models.TourMedia.objects.create(
                media=media,
                tour=tour
            )

        for service in services:
            models.TourService.objects.create(
                service=service,
                tour=tour
            )
        return Response('The tour has been created', status.HTTP_200_OK)
    except:
        return Response('Bad request', status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_tours(request):
    tours = models.Tour.objects.all()
    serializer = serializers.TourSerializer(tours, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def delete_tour(request, pk):
    try:
        tour = models.Tour.objects.get(pk=pk)
        tour_images = models.TourImage.objects.filter(tour=tour)
        tour_videos = models.TourMedia.objects.filter(tour=tour)

        for image in tour_images:
            image.image.delete(save=False)

        for media in tour_videos: 
            media.media.delete(save=False) 

        tour.delete()
        return Response("The tour has been deleted", status.HTTP_200_OK)
    except:
        return Response('Did not find such information', status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def update_tour(request, pk):
    try:
        images = request.FILES.getlist('image')
        videos = request.FILES.getlist('media')
        services = request.POST.getlist('service')

        tour = models.Tour.objects.get(pk=pk)

        tour_images = models.TourImage.objects.filter(tour=tour)
        tour_videos = models.TourMedia.objects.filter(tour=tour)
        tour_services = models.TourService.objects.filter(tour=tour)

        serializer = serializers.TourSerializer(tour, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()

            for image in tour_images:
                image.image.delete(save=False)
                image.delete()

            for image in images:
                models.TourImage.objects.create(
                    image=image,
                    tour=tour
                )

            for media in tour_videos: 
                media.media.delete(save=False)
                media.delete()

            for media in videos:
                models.TourMedia.objects.create(
                    media=media,
                    tour=tour
                )

            for service in tour_services:
                service.delete()

            for service in services:
                models.TourService.objects.create(
                    service=service,
                    tour=tour
                )
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response('Did not find such information', status.HTTP_400_BAD_REQUEST)
    

# Raiting