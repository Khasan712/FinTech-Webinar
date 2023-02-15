from django.db import models
import uuid

# Create your models here.


class Webinar(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class UUIDForWebinar(models.Model):
    webinar = models.ForeignKey(Webinar, on_delete=models.PROTECT, related_name='uuid_webinar')
    uuid = models.CharField(max_length=255, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    domain = models.CharField(max_length=255)
    path_link = models.CharField(max_length=255, blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.path_link:
            self.uuid = uuid.uuid4()
            self.path_link = f'{self.domain}/?web_id={self.uuid}'
        super().save(*args, **kwargs)
