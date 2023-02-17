from django.contrib import admin
from api.v1.register.models import Register, Backend, Mobile, Frontend, Webinar
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class RegisterSourse(resources.ModelResource):
    class Meta:
        model = Register
        fields = ('phone_number',)
        export_order = ('phone_number',)


class BookAdmin(ImportExportModelAdmin):
    resource_classes = [RegisterSourse]

admin.site.register(Register, BookAdmin)

#@admin.register(Register)
#class RegisterAdmin(admin.ModelAdmin):
#    list_display = ('id', 'first_name', 'phone_number', 'course', 'created_at')
#    list_filter = ('course',)


@admin.register(Backend)
class BackendAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone_number', 'created_at')


@admin.register(Frontend)
class FrontendAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone_number', 'created_at')


@admin.register(Mobile)
class MobileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone_number', 'created_at')


@admin.register(Webinar)
class WebinarAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone_number', 'created_at')
