from django.apps import AppConfig
import threading


class ServeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "serve"
