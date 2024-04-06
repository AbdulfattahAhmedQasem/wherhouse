from django.contrib import admin
from .models import UserProfile
from import_export.admin import ImportExportModelAdmin
@admin.register(UserProfile)
class UserProfileImport(ImportExportModelAdmin):
    pass
# Register your models here.
# admin.site.register(UserProfile)
