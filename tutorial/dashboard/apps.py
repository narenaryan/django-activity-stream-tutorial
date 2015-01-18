from django.apps import AppConfig
from actstream import registry
from django.contrib.auth.models import User

class MyAppConfig(AppConfig):
    name = 'dashboard'
    def ready(self):
        registry.register(User,self.get_model('Task'),self.get_model('Supervisor'))