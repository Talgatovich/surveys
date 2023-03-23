from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    username = models.CharField(
        "Логин", max_length=150, unique=True
    )
    password = models.CharField("Пароль", max_length=250)
    first_name = models.CharField("Имя", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)
    email = models.EmailField("E-mail", unique=True)
    balance = models.PositiveSmallIntegerField("Баланс", default=0)
    passed_tests = models.PositiveSmallIntegerField(
        "Пройденные тесты", default=0
    )
    avatar = models.ImageField(
        "Аватар",
        upload_to="users/",
        blank=True
    )
    username_color = models.CharField("Цвет", max_length=50, default="white")
    back_color = models.CharField("Цвет фона", max_length=50, default="white")

    class Meta:
        ordering = ("-pk",)
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name
