from django.contrib import admin
from testform.models import model_testform
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class testformResource(resources.ModelResource):

    class Meta:
        model = model_testform

class testformAdmin(ImportExportModelAdmin):
    resource_class = testformResource

admin.site.register(model_testform, testformAdmin)
