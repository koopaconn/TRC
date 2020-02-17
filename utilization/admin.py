from django.contrib import admin
from utilization.models import model_utilization,model_name,model_project
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class utilizationResource(resources.ModelResource):

    class Meta:
        model = model_utilization

class utilizationAdmin(ImportExportModelAdmin):
    resource_class = utilizationResource

admin.site.register(model_utilization, utilizationAdmin)
admin.site.register(model_name)
admin.site.register(model_project)
