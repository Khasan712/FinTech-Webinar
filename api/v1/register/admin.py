from django.contrib import admin
from api.v1.register.models import Register, Backend, Mobile, Frontend, Webinar
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class RegisterSourse(resources.ModelResource):
    class Meta:
        model = Register
        fields = ('phone_number',)
        export_order = ('phone_number',)


class WebinarSourse(resources.ModelResource):
    class Meta:
        model = Webinar
        fields = ('phone_number',)
        export_order = ('phone_number',)


class BackendSourse(resources.ModelResource):
    class Meta:
        model = Backend
        fields = ('phone_number',)
        export_order = ('phone_number',)


class FrontendSourse(resources.ModelResource):
    class Meta:
        model = Frontend
        fields = ('phone_number',)
        export_order = ('phone_number',)


class MobileSourse(resources.ModelResource):
    class Meta:
        model = Mobile
        fields = ('phone_number',)
        export_order = ('phone_number',)


#  Rgeister
class RegisterImportExport(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [RegisterSourse]


admin.site.register(Register, RegisterImportExport)


#  Webinar
class WebinarImportExport(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [WebinarSourse]


admin.site.register(Webinar, WebinarImportExport)


# Backend
class BackendImportExport(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [BackendSourse]


admin.site.register(Backend, BackendImportExport)


# Frontend
class FrontendImportExport(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [FrontendSourse]


admin.site.register(Frontend, FrontendImportExport)


# Mobile
class MobileImportExport(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [MobileSourse]


admin.site.register(Mobile, MobileImportExport)














# @admin.register(Backend)
# class BackendAdmin(admin.ModelAdmin):
#     list_display = ('id', 'first_name', 'phone_number', 'created_at')
#
#
# @admin.register(Frontend)
# class FrontendAdmin(admin.ModelAdmin):
#     list_display = ('id', 'first_name', 'phone_number', 'created_at')
#
#
# @admin.register(Mobile)
# class MobileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'first_name', 'phone_number', 'created_at')
#
#
# @admin.register(Webinar)
# class WebinarAdmin(admin.ModelAdmin):
#     list_display = ('id', 'first_name', 'phone_number', 'created_at')
