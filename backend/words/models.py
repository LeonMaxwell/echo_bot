from django.db import models
from django.utils.translation import gettext_lazy as _


class Quiz(models.Model):
    user_id = models.CharField(verbose_name="ID пользователя", unique=True, max_length=255)
    age = models.IntegerField(verbose_name="Сколько лет?")
    birth = models.CharField(verbose_name="Где родился?", max_length=255)

    class Meta:
        verbose_name = "Ответы на вопрос"
        verbose_name_plural = "Ответы на вопросы"
        db_table = 'quiz'

    def __str__(self):
        return f"Пользователь № {self.user_id}"


class Answer(models.Model):
    class TypeAnswerChoice(models.TextChoices):
        DEFAULT = "DEF", _("Обычный ответ"),
        ACCESS = "ACS", _("Успешный ввод данных"),
        ERROR = "ERR", _("Ошибка при заполнении")

    type_message = models.CharField(verbose_name="Тип сообщения", max_length=3, unique=True, choices=TypeAnswerChoice.choices,
                                    default=TypeAnswerChoice.DEFAULT)
    message = models.CharField(verbose_name="Сообщение", max_length=255)

    class Meta:
        verbose_name = "Настройка сообщений отправляемые ботом"
        verbose_name_plural = "Настрйоки сообщений отправляемые ботом"
        db_table = 'answer'

    def __str__(self):
        return f"[{self.type_message}] {self.message}"