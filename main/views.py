from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.db import transaction

from . import models
from . import serializers


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