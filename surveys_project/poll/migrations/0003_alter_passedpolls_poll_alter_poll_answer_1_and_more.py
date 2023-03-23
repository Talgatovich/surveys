# Generated by Django 4.1.7 on 2023-03-23 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("poll", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="passedpolls",
            name="poll",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="passed_poll",
                to="poll.poll",
            ),
        ),
        migrations.AlterField(
            model_name="poll",
            name="answer_1",
            field=models.CharField(max_length=300, null=True, verbose_name="Ответ № 1"),
        ),
        migrations.AlterField(
            model_name="poll",
            name="answer_2",
            field=models.CharField(max_length=300, null=True, verbose_name="Ответ № 2"),
        ),
        migrations.AlterField(
            model_name="poll",
            name="answer_3",
            field=models.CharField(max_length=300, null=True, verbose_name="Ответ № 3"),
        ),
        migrations.AlterField(
            model_name="poll",
            name="answer_4",
            field=models.CharField(max_length=300, null=True, verbose_name="Ответ № 4"),
        ),
        migrations.AlterField(
            model_name="poll",
            name="correct_answer",
            field=models.CharField(
                help_text="Выберите номер ответа",
                max_length=20,
                null=True,
                verbose_name="Ответ",
            ),
        ),
        migrations.AlterField(
            model_name="poll",
            name="question",
            field=models.CharField(max_length=300, verbose_name="Вопрос"),
        ),
    ]
