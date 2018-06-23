from django.apps import AppConfig


class BlinksConfig(AppConfig):
    name = 'bci_challenge.blinks'
    verbose_name = "Blinks"

    def ready(self):
        """
        Override this to put in:
        - Blinks system checks
        - Blinks signal registration
        """
        pass
