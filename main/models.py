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
        return self.username
    
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
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    start_time = models.DateField()
    end_time = models.DateField()
    discount = models.IntegerField(default=0)
    cost = models.IntegerField()
    seats = models.IntegerField()


    def __str__(self):
        return f"{self.creator} - {self.title}"
    
    class Meta:
        verbose_name = "Sayohat"
        verbose_name_plural = "Sayohatlar"   
    

class TourImage(models.Model):
    image = models.ImageField(upload_to='tour_images/', null=True, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tour.title} - {self.image}"
    
    class Meta:
        verbose_name = "Rasm"
        verbose_name_plural = "Rasmlar"   


class TourMedia(models.Model):
    media = models.FileField(upload_to='tour_videos/', null=True, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tour.title} - {self.media}"
    
    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Vodeolar"  


class TourService(models.Model):
    service = models.TextField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tour.title} - {self.service}"
    
    class Meta:
        verbose_name = "Xizmat"
        verbose_name_plural = "Xizmatlar"  


class Booking(models.Model):
    for_connect = models.CharField(max_length=255)
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    token = models.TextField()
    STATUS_CHOICES = (
        (1, 'Bron qilingan'),
        (2, 'To`langan'),
        (3, 'Bekor qilingan'),
    )

    status = models.SmallIntegerField(
        choices=STATUS_CHOICES
    )

    def __str__(self):
        return f"{self.buyer.username} - {self.tour.title}"

    class Meta:
        verbose_name = "Bron"
        verbose_name_plural = "Bronlar"  


class Feedbag(models.Model):
    status = models.BooleanField(default=False)
    description = models.TextField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}) {self.author.username} - {self.tour.title}"

    class Meta:
        verbose_name = "Izox"
        verbose_name_plural = "Izohlar"  


class Raiting(models.Model):
    grade = models.SmallIntegerField()
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.username} - {self.tour.title}"

    class Meta:
        verbose_name = "Baho"
        verbose_name_plural = "Baholar"  