# Generated by Django 4.1.7 on 2023-03-22 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Poll",
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
                ("question", models.CharField(max_length=200, verbose_name="Вопрос")),
                (
                    "answer_1",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Ответ № 1"
                    ),
                ),
                (
                    "answer_2",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Ответ № 2"
                    ),
                ),
                (
                    "answer_3",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Ответ № 3"
                    ),
                ),
                (
                    "answer_4",
                    models.CharField(
                        max_length=200, null=True, verbose_name="Ответ № 4"
                    ),
                ),
                (
                    "correct_answer",
                    models.CharField(
                        help_text="Выберите номер ответа",
                        max_length=200,
                        null=True,
                        verbose_name="Ответ",
                    ),
                ),
            ],
            options={
                "verbose_name": "Тест",
                "verbose_name_plural": "Тесты",
                "ordering": ("-pk",),
            },
        ),
        migrations.CreateModel(
            name="PassedPolls",
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
                    "poll",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="poll.poll"
                    ),
                ),
            ],
            options={
                "verbose_name": "Пройденный тест пользователя",
                "verbose_name_plural": "Пройденные тесты пользователя",
                "ordering": ("-pk",),
            },
        ),
    ]