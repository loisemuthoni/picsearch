from django.apps import AppConfig


class PicConfig(AppConfig):
    name = 'pic'

    def ready(self):
        import users.signals