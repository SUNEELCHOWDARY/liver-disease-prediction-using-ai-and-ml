from django.contrib import admin

# Register your models here.
from .models import HealthAssessment,UserImageModel

admin.site.register(HealthAssessment)
admin.site.register(UserImageModel)