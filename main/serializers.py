from rest_framework import serializers
from . import models

class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tour_image
        fields = ('path',)

class TourVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tour_video
        fields = ('path',)

class TourServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tour_service
        fields = ('description',)

class TourSerializer(serializers.ModelSerializer):
    images = TourImageSerializer(many=True, required=False)
    videos = TourVideoSerializer(many=True, required=False)
    services = TourServiceSerializer(many=True, required=False)

    class Meta:
        model = models.Tour
        fields = ('name', 'description', 'cost', 'start_time', 'end_time', 'images', 'videos', 'services')

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        videos_data = validated_data.pop('videos', [])
        services_data = validated_data.pop('services', [])

        tour = models.Tour.objects.create(**validated_data)

        for image_data in images_data:
            models.Tour_image.objects.create(tour=tour, **image_data)

        for video_data in videos_data:
            models.Tour_video.objects.create(tour=tour, **video_data)

        for service_data in services_data:
            models.Tour_service.objects.create(tour=tour, **service_data)

        return tour