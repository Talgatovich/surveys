from django.db import models
from django.utils.translation import gettext as _
from users.models import User


class Poll(models.Model):
    """Модель опроса."""

    question = models.CharField(
        "Вопрос",
        max_length=200
    )
    answer_1 = models.CharField("Ответ № 1", max_length=200, null=True)
    answer_2 = models.CharField("Ответ № 2", max_length=200, null=True)
    answer_3 = models.CharField("Ответ № 3", max_length=200, null=True)
    answer_4 = models.CharField("Ответ № 4", max_length=200, null=True)
    correct_answer = models.CharField(
        "Ответ",
        max_length=200,
        null=True,
        help_text="Выберите номер ответа",
    )

    class Meta:
        ordering = ("-pk",)
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    def __str__(self):
        return self.question


class PassedPolls(models.Model):
    """Связующая модель для пройденных пользователям тестов."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-pk",)
        verbose_name = "Пройденный тест пользователя"
        verbose_name_plural = "Пройденные тесты пользователя"

    def __str__(self):
        return f"{self.user.username} прошел {self.poll.id}"
