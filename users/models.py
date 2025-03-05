from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=20,
        verbose_name="псевдоним",
        unique=True,
    )

    def __str__(self):
        return f"{self.pk} {self.username}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
