from django.db.models import manager


class BackendManager(manager.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(course="backend")


class FrontendManager(manager.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(course="frontend")


class MobileManager(manager.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(course="mobile")

