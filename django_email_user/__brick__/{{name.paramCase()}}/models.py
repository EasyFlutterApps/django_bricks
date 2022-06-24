from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=25, blank=True, null=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
