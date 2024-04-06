from django.db import models
from datetime import datetime
class category(models.Model):
    name = models.CharField(max_length=150)
    photocat = models.ImageField(upload_to='cate/%Y/%m/%d/')
    def __str__(self):
        return self.name
    class Meta:
        ordering:['-name'] # type: ignore
class product(models.Model):
    categorys     = models.ForeignKey(category, on_delete=models.CASCADE, default=1)
    name          = models.CharField(max_length=150)
    photo         = models.ImageField(upload_to='photo/%Y/%m/%d/',null=True)
    typeproduct   = models.CharField(max_length=255, null=True, blank=True)
    shapeproduct = models.CharField(max_length=255, null=True, blank=True)
    quantityproduct = models.IntegerField(default=1) 
    productlength = models.DecimalField(max_digits=5, decimal_places=2, null=True,blank=True)
    productwidth  = models.DecimalField(max_digits=5, decimal_places=2, null=True,blank=True)
    productheight = models.DecimalField(max_digits=5, decimal_places=2, null=True,blank=True)
   
    # publish_date = models.DateTimeField(default = datetime.now)
    def __str__(self):
        return self.name
    class Meta:
        ordering:['-publish_date'] # type: ignore
##################models
class yourmodels(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
class modelNotices(models.Model):
    imageNotices = models.ImageField(upload_to='imageNotices/%y/%m/%d/')
    def __str__(self):
        return f"image:{self.imageNotices}"
    class Meta:
        ordering:['imageNotices'] # type: ignore