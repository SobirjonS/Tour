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


class TourFeedbagAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AnswerFeedbag
        fields = ['answer']


class TourFeedbagSerializer(serializers.ModelSerializer):
    answer = TourFeedbagAnswerSerializer(source='answerfeedbag_set', many=True, read_only=True)
    class Meta:
        model = models.Feedbag
        fields = ['feedbag', 'answer']


class TourRaitingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Raiting
        fields = ['grade']


class TourSerializer(serializers.ModelSerializer):
    services = TourServiceSerializer(source='tourservice_set', many=True, read_only=True)
    images = TourImageSerializer(source='tourimage_set', many=True, read_only=True)
    media = TourMediaSerializer(source='tourmedia_set', many=True, read_only=True)
    feedbag = TourFeedbagSerializer(source='feedbag_set', many=True, read_only=True)

    class Meta:
        model = models.Tour
        fields = [
            'id', 'category', 'place_name', 'title', 'body', 'start_time', 'end_time',
            'discount', 'cost', 'seats', 'services', 'images', 'media', 'feedbag', 'raiting'
        ]


class BookingTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tour
        fields = ['title', 'start_time', 'end_time']


class BookingSerializer(serializers.ModelSerializer):
    tour = BookingTourSerializer(read_only=True)
    buyer = serializers.CharField(source='buyer.username', read_only=True)
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.get_status_display()

    class Meta:
        model = models.Booking
        fields = ['id', 'created_at', 'for_connect', 'seats', 'token', 'status', 'buyer', 'tour']
