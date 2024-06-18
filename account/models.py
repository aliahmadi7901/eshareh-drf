from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True, verbose_name="شماره موبایل")
    image = models.ImageField(upload_to="users", verbose_name="تصویر کاربر")

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
