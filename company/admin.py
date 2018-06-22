from django.contrib import admin
from company.models import Invitees
from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin

admin.site.site_header = "MAZARS BRJ LAUNCH PAD"

class InviteesResource(ModelResource):
    class Meta:
        model = Invitees
        verbose_name = ('Invited Guests')

class InviteesAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = InviteesResource
    list_display =('name','company','designation','category','status','date_of_update','telephone_contact','email_address','comments')
    import_order =('name','company','designation','category','status','date_of_update','telephone_contact','email_address','comments')
    list_filter = ('category','status')
    search_fields = ['name',]


admin.site.register(Invitees,InviteesAdmin)
