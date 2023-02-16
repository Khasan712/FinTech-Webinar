from django.contrib import admin
from api.v1.register.models import Register, Backend, Mobile, Frontend


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone_number', 'webinar', 'created_at')
    list_filter = ('webinar',)


@admin.register(Backend)
class BackendAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone_number', 'created_at')


@admin.register(Frontend)
class FrontendAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone_number', 'created_at')


@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone_number', 'created_at')
