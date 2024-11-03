from django.contrib import admin
from .models import *


# Register your models here.
class AdminProfile(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "email",
    )


admin.site.register(Profile, AdminProfile)
