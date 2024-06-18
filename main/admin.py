from django.contrib import admin
from . import models

admin.site.register(models.CustomUser)
admin.site.register(models.Tour)
admin.site.register(models.TourImage)
admin.site.register(models.TourVideo)
admin.site.register(models.TourService)
admin.site.register(models.Book)
admin.site.register(models.TourSeat)
admin.site.register(models.Feedbag)
admin.site.register(models.Raiting)
