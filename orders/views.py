from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from httpcore import request
from product.models import product
from orders.models import JobOrderForm, Order,OrderDetails, JobOrderForm
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import JobOrderForm
from django.core.files.base import ContentFile
from django.core.exceptions import ObjectDoesNotExist
#########################################################import pdf
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
########################################################end
# from django.core.mail import send_mail
# # Create your views here.
def add_to_cart(request,pro_id):
  #التاكد من المدخلات
  if 'proid' in request.GET and 'quty' in request.GET  and request.user.is_authenticated and not request.user.is_anonymous:
     # get productid and quntity form get
     proids = request.GET['proid']
     qut = request.GET['quty']
     #filter to sure the order is old or not oldالتحقق من ان المستخدم لة طلب لم ينتهي 
     order = Order.objects.all().filter(user = request.user, is_finished = False)
     #التحقق من ان المنتج موجود فعلا 
     if not product.objects.all().filter(id=proids).exists():
       return redirect('index')
     #جلب المنتج من اجل ادخالة لسلة المشتريات 
     pro = product.objects.get(id = proids)
     #the order is old order
     if order:
       #get the order olde from the user=user and state order is not finish
       old_order = Order.objects.get(user = request.user , is_finished = False)
       ####################################################### في حالة السعر متغير لايفضل اضافة هذة الميزةفي حال السعر متغير 
       if OrderDetails.objects.all().filter(order = old_order,product=pro).exists():
          order = OrderDetails.objects.get(order = old_order,product=pro)
          if pro.quantityproduct >=int(qut):
            pro.quantityproduct -=int(qut)
            order.quantity +=int(qut)
            pro.save()
            order.save() 
          else:
            messages.error(request,"كمية المنتج اقل من الكمية المطلوبة")
      ####################################################  
       else:
       #after get order work add ordersdetails from the same order
        if pro.quantityproduct >= int(qut):
          pro.quantityproduct -=int(qut)
          orderDetails = OrderDetails.objects.create(order = old_order,product = pro ,quantity = qut)
       #save orders
          pro.save()
          orderDetails.save()
          messages.success(request,'was added to cart for old order')
        else:
            messages.error(request,"كمية المنتج اقل من الكمية المطلوبة")
     else:
       if pro.quantityproduct >= int(qut):  
         #create new object from order
         new_order = Order()
         #get the username from the request
         new_order.user = request.user
         #get the time add order
         #get state orders 
         new_order.is_finished = False
         #save orders
         new_order.save()
         #get all ordersdetails from reqist
         pro.quantityproduct -=int(qut)
         orderDetails = OrderDetails.objects.create(order = new_order,product = pro,quantity = qut)
         #save the ordersdetails
         pro.save()
         orderDetails.save()
         messages.success(request,"was added to cart for new order")
       else:
         messages.error(request,"كمية المنتج اقل من الكمية المطلوبة")
        #return the same page 
     return redirect('/product/showdetails/'+str(pro_id))
  else:
    return redirect('index')
def showCart(request):
  context = None
  if request.user.is_authenticated and not request.user.is_anonymous:
    if Order.objects.all().filter(user = request.user , is_finished = False):
      order = Order.objects.get(user = request.user,is_finished = False)
      orderdetails = OrderDetails.objects.all().filter(order = order)
      context = {
        'order':order,
        'details':orderdetails
      }
  return render(request,'order/cart.html',context)
def delete_cart(request,orderdetalsid):
  if request.user.is_authenticated and not request.user.is_anonymous and orderdetalsid:
    order = OrderDetails.objects.get(id = orderdetalsid)
    pro = product.objects.get(id = order.product.id)
    if order.order.user.id == request.user.id:
      pro.quantityproduct += order.quantity
      pro.save()
      order.delete()
  return redirect('showCart')
def add_qty(request,orderdetalsid):
  if request.user.is_authenticated and not request.user.is_anonymous and orderdetalsid:
    order = OrderDetails.objects.get(id = orderdetalsid)
    if order.order.user.id == request.user.id:
      pro = product.objects.get(id = order.product.id)
      if pro.quantityproduct > 0:
        order.quantity +=1
        pro.quantityproduct -= 1
        order.save()
        pro.save()
      else:
        messages.error(request,"كمية المطلوبة اكثر من كمية المنتج الحالي  ")
  return redirect('showCart')
def sub_qtu(request,orderdetalsid):
  if request.user.is_authenticated and not request.user.is_anonymous and orderdetalsid:
    order = OrderDetails.objects.get(id=orderdetalsid)
    if order.order.user.id == request.user.id:
      pro = product.objects.get(id = order.product.id)
      if order.quantity>1:
        pro.quantityproduct +=1
        order.quantity -=1
        pro.save()
        order.save()
      else:
        pro.quantityproduct += order.quantity
        pro.save()
        order.delete()
        
  return redirect('showCart')
def pyment(request):
  if request.user.is_authenticated and not request.user.is_anonymous:
    order = Order.objects.get(user = request.user,is_finished = False)
    order.is_finished = True
    order.save()
  return render(request,'order/pyment.html')

def show_orders(request):
  context = None
  all_orders = None
  if request.user.is_authenticated and not request.user.is_anonymous:
    all_orders = Order.objects.all().filter(user=request.user)
    if all_orders:
      for x in all_orders:
        order = Order.objects.get(id = x.id) 
        orderDetails = OrderDetails.objects.all().filter(order = order)
        for sub in orderDetails:
          pass
        x.items_count = orderDetails.count
      context = {
        "all_order":all_orders
      }
  return render(request,'order/show_orders.html',context)

def shownumberjob(request):
  return render(request,'order/order_form.html')

def joborder(request):
    if request.method == 'POST':
        numid = request.POST.get('numberproject', None)
        date = timezone.now()
        jobOrderType = request.POST.get('jobOrderType', None)
        proimg = request.FILES.get('proimg', None)
        pdffile = request.FILES.get('pdffile', None)
        clientName = request.POST.get('clientName', None)
        coordination = request.POST.get('coordination', None)
        projectManager = request.POST.get('projectManager', None)
        venueLocation = request.POST.get('venueLocation', None)
        installationDate = request.POST.get('installationDate', None)
        installationTime = request.POST.get('installationTime', None)
        openingDate = request.POST.get('openingDate', None)
        openingTime = request.POST.get('openingTime', None)
        dismantleDate = request.POST.get('dismantleDate', None)
        dismantleTime = request.POST.get('dismantleTime', None)
        handOverDateTime = request.POST.get('handOverDateTime', None)
        note = request.POST.get('note', None)
        if all([numid, date, jobOrderType, proimg, pdffile, clientName, coordination, projectManager, venueLocation,
                installationDate, installationTime, openingDate, openingTime, dismantleDate, dismantleTime, handOverDateTime, note]):
            job_order = JobOrderForm(
                numberproject=numid,
                date=date,
                jobOrderType=jobOrderType,
                clientName=clientName,
                coordination=coordination,
                projectManager=projectManager,
                venueLocation=venueLocation,
                installationDate=installationDate,
                installationTime=installationTime,
                openingDate=openingDate,
                openingTime=openingTime,
                dismantleDate=dismantleDate,
                dismantleTime=dismantleTime,
                handOverDateTime=handOverDateTime,
                note=note)
            if proimg:
              file_content = proimg.read()
              job_order.proimg.save(f"{job_order.numberproject}_proimg.{proimg.name.split('.')[-1]}",ContentFile(file_content))
            if pdffile:
               pdffile_content = pdffile.read()
               job_order.pdffile.save(f"{job_order.numberproject}_pdffile.{pdffile.name.split('.')[-1]}",ContentFile(pdffile_content))
            try:   
              orders =Order.objects.get(user = request.user,is_finished=False)
              orders.is_finished = True
              orders.jobordernumber = job_order.numberproject
              orders.save()
              job_order.save()
            except ObjectDoesNotExist:
                return render(request, 'order/order_form.html',messages.error(request,'Order matching query does not exist.'))
              
            return render(request, 'order/order_form.html',messages.success(request,'Job order submitted successfully'))
        else:
            return render(request, 'order/order_form.html',messages.error(request,'Missing required fields'))
    else:
        return render(request, 'order/order_form.html',messages.error(request,'Missing required fields post'))
##############################################timer
# import schedule
# import time
# from datetime import datetime, timedelta
# def sendtime():
#     reservation_date = datetime.now().date()
#     event_date = reservation_date - timedelta(days=3)
#     date_today = datetime.now().date()
#     if date_today == event_date:
#         print("hdejieji")
#     else:
#         print("there is not event now")

# schedule.every().day.at("12:00").do(sendtime)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

#############################################time
