from rest_framework import serializers
from . import models


# Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


# Tour
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




