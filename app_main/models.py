from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(verbose_name="Telefon raqam", null=True, blank=True)
    profile_image = models.ImageField(verbose_name="Profile Image", upload_to="profiles/", null=True, blank=True)
    address = models.CharField(verbose_name="Address", max_length=255)


class Product(models.Model):
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    name = models.CharField(verbose_name="Maxsulot nomi", max_length=50, unique=True)
    price = models.DecimalField(verbose_name="Maxsulot narxi", max_digits=12, decimal_places=2)
    image = models.ImageField(verbose_name="Maxsulot rasmi", upload_to="media/", null=True, blank=True)

    def __str__(self):
        return self.name
