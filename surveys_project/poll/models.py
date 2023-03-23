from django.db import models


from users.models import User


class Poll(models.Model):
    """Модель опроса."""

    question = models.CharField("Вопрос", max_length=300)
    answer_1 = models.CharField("Ответ № 1", max_length=300, null=True)
    answer_2 = models.CharField("Ответ № 2", max_length=300, null=True)
    answer_3 = models.CharField("Ответ № 3", max_length=300, null=True)
    answer_4 = models.CharField("Ответ № 4", max_length=300, null=True)
    correct_answer = models.CharField(
        "Ответ",
        max_length=20,
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
    """Связующая модель для пройденных тестов."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="passed_poll")

    class Meta:
        ordering = ("-pk",)
        verbose_name = "Пройденный тест пользователя"
        verbose_name_plural = "Пройденные тесты пользователя"

    def __str__(self):
        return f"{self.user.username} - {self.poll.id}"
