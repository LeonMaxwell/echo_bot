from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WordsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'words'
    verbose_name = _("Информация бота")
