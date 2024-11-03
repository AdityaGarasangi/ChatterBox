from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, null=False)
    email = models.EmailField(max_length=254)
    image = models.ImageField(
        default="images/default.jpg", upload_to="images", blank=True
    )

    def __str__(self):
        return self.name
