from rest_framework import serializers
from . import models


class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TourImage
        fields = ('image',)


class TourVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TourVideo
        fields = ('media',)


class TourServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TourService
        fields = ('service_description',)


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TourSeat
        fields = ('seats')


class TourSerializer(serializers.ModelSerializer):
    images = TourImageSerializer(many=True, required=False)
    videos = TourVideoSerializer(many=True, required=False)
    services = TourServiceSerializer(many=True, required=False)
    seats = serializers.IntegerField()

    class Meta:
        model = models.Tour
        fields = ('name', 'description', 'cost', 'start_time', 'end_time', 'images', 'videos', 'services', 'seats')

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        videos_data = validated_data.pop('videos', [])
        services_data = validated_data.pop('services', [])
        seats = validated_data.pop('seats') 

        tour = models.Tour.objects.create(**validated_data)

        seat = models.TourSeat.objects.create(
            tour=tour,
            seats=seats,
        )

        for image_data in images_data:
            models.TourImage.objects.create(tour=tour, **image_data)

        for video_data in videos_data:
            models.TourVideo.objects.create(tour=tour, **video_data)

        for service_data in services_data:
            models.TourService.objects.create(tour=tour, **service_data)

        return tour
