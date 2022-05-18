from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        # this is just how the django doc recommends 
        # to avoid import conflicts
        import users.signals
