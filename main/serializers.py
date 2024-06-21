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

    
    def create(self, validated_data):
        services_data = validated_data.pop('tourservice_set')
        images_data = validated_data.pop('tourimage_set')
        media_data = validated_data.pop('tourmedia_set')
        tour = models.Tour.objects.create(**validated_data)
        
        for service_data in services_data:
            models.TourService.objects.create(tour=tour, **service_data)
        
        for image_data in images_data:
            models.TourImage.objects.create(tour=tour, **image_data)
        
        for media_data in media_data:
            models.TourMedia.objects.create(tour=tour, **media_data)
        
        return tour

    def update(self, instance, validated_data):
        services_data = validated_data.pop('tourservice_set', [])
        images_data = validated_data.pop('tourimage_set', [])
        media_data = validated_data.pop('tourmedia_set', [])

        instance.category = validated_data.get('category', instance.category)
        instance.creator = validated_data.get('creator', instance.creator)
        instance.place_name = validated_data.get('place_name', instance.place_name)
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.seats = validated_data.get('seats', instance.seats)
        instance.save()

        # Обновление услуг
        if services_data:
            models.TourService.objects.filter(tour=instance).delete()
            for service_data in services_data:
                models.TourService.objects.create(tour=instance, **service_data)
        
        # Обновление изображений
        if images_data:
            models.TourImage.objects.filter(tour=instance).delete()
            for image_data in images_data:
                models.TourImage.objects.create(tour=instance, **image_data)
        
        # Обновление медиа
        if media_data:
            models.TourMedia.objects.filter(tour=instance).delete()
            for media_data in media_data:
                models.TourMedia.objects.create(tour=instance, **media_data)

        return instance
