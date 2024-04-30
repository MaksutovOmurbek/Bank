from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(
        max_length=255, verbose_name="Номер телефона"
    )

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class YourModel(models.Model):
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\(\+996\)\d{9}$')])

    def save(self, *args, **kwargs):
       
        super().save(*args, **kwargs)
