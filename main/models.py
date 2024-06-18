from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='author_avatas/', null=True, blank=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'


class Tour(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.IntegerField()
    start_time = models.DateField()
    end_time = models.DateField()
    

class TourImage(models.Model):
    image = models.ImageField(upload_to='tour_images/', null=True, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)


class TourVideo(models.Model):
    media = models.FileField(upload_to='tour_videos/', null=True, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)


class TourService(models.Model):
    service_description = models.TextField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)


class Book(models.Model):
    seats = models.IntegerField()
    for_connect = models.CharField(max_length=255)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.TextField()
    STATUS_CHOICES = (
        (1, 'Bron qilingan'),
        (2, 'To`langan'),
        (3, 'Bekor qilingan'),
    )

    status = models.SmallIntegerField(
        choices=STATUS_CHOICES
    )
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)


class TourSeat(models.Model):
    seats = models.IntegerField()
    tour =  models.ForeignKey(Tour, on_delete=models.CASCADE)


class Feedbag(models.Model):
    description = models.TextField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Raiting(models.Model):
    grade = models.SmallIntegerField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)