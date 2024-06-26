from rest_framework import serializers
from . import models


# Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


# Tour
class TourServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TourService
        fields = ['service']

class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TourImage
        fields = ['image']

class TourMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TourMedia
        fields = ['media']

class TourSerializer(serializers.ModelSerializer):
    services = TourServiceSerializer(source='tourservice_set', many=True, read_only=True)
    images = TourImageSerializer(source='tourimage_set', many=True, read_only=True)
    media = TourMediaSerializer(source='tourmedia_set', many=True, read_only=True)

    class Meta:
        model = models.Tour
        fields = [
            'id', 'category', 'place_name', 'title', 'body', 'start_time', 'end_time',
            'discount', 'cost', 'seats', 'services', 'images', 'media'
        ]



class BookingTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tour
        fields = ['title', 'start_time', 'end_time']


class BookingSerializer(serializers.ModelSerializer):
    tour = BookingTourSerializer(many=True, read_only=True)

    class Meta:
        model = models.Booking
        fields = ['status']