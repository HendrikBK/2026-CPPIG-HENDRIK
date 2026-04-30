from django.apps import AppConfig


class ReservasConfig(AppConfig):
    name = 'reservas'

    def ready(self):
        from .utils.scheduler import start
        start()
