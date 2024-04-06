from import_export import resources
from .models import category,product
class CategoryResources(resources.ModelResource):
    class Meta:
        model = category
class ProductResources(resources.ModelResource):
    class Meta:
        model = product