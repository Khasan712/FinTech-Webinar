from django.db import models

from api.v1.register.enums import Course
from api.v1.register.managers import FrontendManager, BackendManager, MobileManager
from api.v1.webinar.models import Webinar


# Create your models here.


class Register(models.Model):
    first_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    webinar = models.ForeignKey(Webinar, on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.CharField(max_length=255, choices=Course.choices(), blank=True, null=True)

    class Meta:
        verbose_name = 'Vebinar'
        verbose_name_plural = 'Vebinar'

    def __str__(self):
        return f'{self.first_name} - {self.phone_number}'


class Backend(Register):
    objects = BackendManager()

    class Meta:
        proxy = True
        verbose_name = 'Backend'
        verbose_name_plural = 'Backendchilar'


class Frontend(Register):
    objects = FrontendManager()

    class Meta:
        proxy = True
        verbose_name = 'Frontchi'
        verbose_name_plural = 'Frontchilar'


class Mobile(Register):
    objects = MobileManager()

    class Meta:
        proxy = True
        verbose_name = 'Mobile'
        verbose_name_plural = 'Mobilchilar'
