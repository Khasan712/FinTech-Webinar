from django.contrib import admin
from api.v1.webinar.models import Webinar, UUIDForWebinar


@admin.register(Webinar)
class WebinarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')


@admin.register(UUIDForWebinar)
class UUIDForWebinarAdmin(admin.ModelAdmin):
    list_display = ('id', 'webinar', 'created_at', 'is_active', 'path_link')

