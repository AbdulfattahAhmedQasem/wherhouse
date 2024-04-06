from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from product.models import product

# Create your models here.
#create models order 

class JobOrderForm(models.Model):
    ordertype = (
        ('sample', 'عينة'),
        ('rent', 'إيجار'),
        ('sale', 'بيع')
    )
    numberproject = models.BigIntegerField()
    date = models.DateField()
    jobOrderType = models.CharField(max_length=100, choices=ordertype)
    clientName = models.CharField(max_length=100)
    coordination = models.CharField(max_length=100)
    projectManager = models.CharField(max_length=100)
    venueLocation = models.CharField(max_length=100)  # Add max_length
    installationDate = models.DateField()
    installationTime = models.TimeField()
    openingDate = models.DateField()
    openingTime = models.TimeField()
    dismantleDate = models.DateField()
    dismantleTime = models.TimeField()
    handOverDateTime = models.DateTimeField()
    note = models.CharField(max_length=250,)
    proimg = models.ImageField(upload_to='proimg/%Y/%m/%d/')
    pdffile = models.FileField(upload_to='uploads/pdffiles/')
    is_Finished = models.BooleanField(default=False,)

    def __str__(self):
        return f'numberproject: {self.numberproject}, orderid: {self.id}'

class Order(models.Model):
    jobordernumber = models.IntegerField(default=0,editable=False)
    #create column contain userid
    user = models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    #create column contain orderdate
    #create column containt about state order
    is_finished = models.BooleanField()
    total = 0
    items_count = 0
    status = models.CharField(max_length=1, choices=[('p', 'Published'), ('d', 'Draft')])
    #create function work retun about order models went we accese the value 
    def __str__(self): 
        return 'user:' +self.user.username+"orderid"+str(self.id)
#create orderDetails

class OrderDetails(models.Model):
    order = models.ForeignKey( Order , on_delete = models.CASCADE ,editable=False)
    product =models.ForeignKey(product,on_delete = models.CASCADE)
    #price = models.DecimalField(max_digits = 6,decimal_places = 2)
    quantity = models.IntegerField()
    def __str__(self):
       return f"user: {self.order.user.username}, product: {self.product.name}, orderid: {self.order.id}"

    #this class work order the product orgenisation about order
    class Meta:
        ordering = ['id']

    
