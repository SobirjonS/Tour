from django.contrib import admin
from . import models

admin.site.register(models.CustomUser)
admin.site.register(models.Tour)
admin.site.register(models.Tour_image)
admin.site.register(models.Tour_video)
admin.site.register(models.Tour_service)
admin.site.register(models.Book)
admin.site.register(models.Seat)
admin.site.register(models.Feedbag)
admin.site.register(models.Raiting)
