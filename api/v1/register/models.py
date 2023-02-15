from django.db import models

from api.v1.webinar.models import Webinar


# Create your models here.


class Register(models.Model):
    first_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    webinar = models.ForeignKey(Webinar, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} - {self.phone_number}'

