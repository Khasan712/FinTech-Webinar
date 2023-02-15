from django.contrib import admin
from api.v1.register.models import Register


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone_number', 'webinar', 'created_at')

