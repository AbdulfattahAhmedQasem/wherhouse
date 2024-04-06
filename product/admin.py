from django.contrib import admin
from .models import product, category, modelNotices
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html

# Define an admin class for the Category model
@admin.register(category)
class CategoryImport(ImportExportModelAdmin):
    # Specify the fields to be displayed in the admin list view for Category
    list_display = ['id', 'name', 'get_image']

    # Define a method to get and display the image for each Category instance
    def get_image(self, obj):
        # Check if the photocat field (image) is available for the Category instance
        if obj.photocat:
            # Display the image with a width of 80 pixels
            return format_html(f"<img src='{obj.photocat.url}' width='80'/>")
        # If no image is available, show a default message
        return 'Image not available' 

    # Set a short description for the image column in the admin list view
    get_image.short_description = "imagecate"

# Define an admin class for the Product model
@admin.register(product)
class ProductAdmin(ImportExportModelAdmin):
    # Specify the fields to be displayed in the admin list view for Product
    list_display = [ 'id','name','typeproduct','shapeproduct','quantityproduct','productlength','productwidth','productheight','get_image'] ##+ [field.name for field in product._meta.fields if field.name != 'photo']
    search_fields=['name','shapeproduct','productlength']
    # Define a method to get and display the image for each Product instance
    def get_image(self, obj):
        # Check if the photo field (image) is available for the Product instance
        if obj.photo:
            # Display the image with a width of 80 pixels
            return format_html(f"<img src='{obj.photo.url}' width='60'/>")
        # If no image is available, show a default message
        return 'Image not available'

    # Set a short description for the image column in the admin list view
    get_image.short_description = 'Image'

# Define an admin class for the modelNotices model
class showimage(admin.ModelAdmin):
    # Specify the fields to be displayed in the admin list view for modelNotices
    list_display = ['id', 'get_image']

    # Define a method to get and display the image for each modelNotices instance
    def get_image(self, obj):
        # Check if the imageNotices field (image) is available for the modelNotices instance
        if obj.imageNotices:
            # Display the image with a width of 80 pixels
            return format_html(f"<img src='{obj.imageNotices.url}' width='80'/>")
        # If no image is available, show a default message
        return 'The image is not available'        

# Register the showimage admin class for the modelNotices model
admin.site.register(modelNotices, showimage)
