# Generated by Django 4.1.7 on 2023-03-23 16:01

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "username",
                    models.CharField(max_length=150, unique=True, verbose_name="Логин"),
                ),
                ("password", models.CharField(max_length=250, verbose_name="Пароль")),
                ("first_name", models.CharField(max_length=150, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=150, verbose_name="Фамилия")),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="E-mail"
                    ),
                ),
                (
                    "balance",
                    models.PositiveSmallIntegerField(default=0, verbose_name="Баланс"),
                ),
                (
                    "passed_tests",
                    models.PositiveSmallIntegerField(
                        default=0, verbose_name="Пройденные тесты"
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True, upload_to="users/", verbose_name="Аватар"
                    ),
                ),
                (
                    "username_color",
                    models.CharField(
                        default="white", max_length=50, verbose_name="Цвет"
                    ),
                ),
                (
                    "back_color",
                    models.CharField(
                        default="white", max_length=50, verbose_name="Цвет фона"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
                "ordering": ("-pk",),
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
