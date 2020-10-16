from django.contrib import admin
from .models import person,education,experience,whole,FilesUpload

@admin.register(person,education,experience,whole)
class UserAdmin(admin.ModelAdmin):
    #list_display=['firstname','lastname']
    pass


admin.site.register(FilesUpload)