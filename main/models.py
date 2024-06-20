from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='author_avatas/', null=True, blank=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"   


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"   


class Tour(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.IntegerField()
    start_time = models.DateField()
    end_time = models.DateField()
    seats = models.IntegerField()

    def __str__(self):
        return f"{self.owner.first_name} - {self.name}"
    
    class Meta:
        verbose_name = "Sayohat"
        verbose_name_plural = "Sayohatlar"   
    

class TourImage(models.Model):
    image = models.ImageField(upload_to='tour_images/', null=True, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tour.name} - {self.image}"
    
    class Meta:
        verbose_name = "Rasm"
        verbose_name_plural = "Rasmlar"   


class TourVideo(models.Model):
    media = models.FileField(upload_to='tour_videos/', null=True, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tour.name} - {self.media}"
    
    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Vodeolar"  


class TourService(models.Model):
    service_description = models.TextField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tour.name} - {self.service_description}"
    
    class Meta:
        verbose_name = "Xizmat"
        verbose_name_plural = "Xizmatlar"  


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

    def __str__(self):
        return f"{self.author.first_name} {self.tour.name}"

    class Meta:
        verbose_name = "Bron"
        verbose_name_plural = "Bronlar"  


class Feedbag(models.Model):
    description = models.TextField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.first_name} {self.tour.name}"

    class Meta:
        verbose_name = "Izox"
        verbose_name_plural = "Izohlar"  


class Raiting(models.Model):
    grade = models.SmallIntegerField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.first_name} {self.tour.name}"

    class Meta:
        verbose_name = "Baho"
        verbose_name_plural = "Baholar"  