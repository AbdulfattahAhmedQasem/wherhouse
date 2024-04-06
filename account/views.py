from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User # visitor the user and add the rest of the data
from .models import UserProfile #visitor the model of the user which the contains the rest of the data
import re
from django.contrib import auth # called the auth to signin in the website
from product.models import product
# Create your views here.
def sinin(request):
    if request.method == "POST" and 'btnlogin' in request.POST:
        username = None
        password = None
        if 'name' in request.POST:username = request.POST['name']
        if 'password' in request.POST:password = request.POST['password']
        if username and password:
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request,'succec login now')
              
            else:
                messages.error(request,'the name or password is invield')
        else:
            messages.error(request,'check the form is empty')
        return render(request,'account/sinin.html',{
            'name':username,
            'password':password
        })
    else:
        return render(request,'account/sinin.html')
def sinup(request):
    if request.method == "POST":
        sinup_name=None
        sinup_email = None
        sinup_password = None
        sinpu_address = None
        sinup_city = None
        sinup_accept = None
        is_add = None
        if 'username' in request.POST:sinup_name=request.POST['username']
        else:messages.error(request,"Error in the name")
        if 'email'in request.POST:sinup_email = request.POST['email']
        else:messages.error(request,'error in the email')
        if 'password' in request.POST:sinup_password = request.POST['password']
        else:messages.error(request,'Error in the password')
        if 'address' in request.POST: sinpu_address = request.POST['address']
        else:messages.error(request,'Error in the address')
        if 'city' in request.POST: sinup_city = request.POST['city']
        else:messages.error(request,'error in the city')
        if 'accept' in request.POST:sinup_accept = request.POST['accept']
        if sinup_name and sinup_email and sinup_password and sinpu_address and sinup_city:
            # check if the clack tems
            if sinup_accept == 'on':
                #check if the username is taken
                if User.objects.filter(username=sinup_name).exists():
                    messages.error(request,'the username is taken change this user ')
                else:
                    #check if the email is taken
                    if User.objects.filter(email=sinup_email).exists():
                        messages.error(request,'the email is taken')
                    else:
                        patt="^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
                        if re.match(patt,sinup_email):
                            # add user
                            user = User.objects.create_user(username=sinup_name,email=sinup_email,password=sinup_password)
                            user.save()
                            #add userprofile
                            userporfile = UserProfile(user=user,address=sinpu_address,city=sinup_city)
                            userporfile.save()
                            sinup_name = ""
                            sinup_email = ""
                            sinup_password = ""
                            sinpu_address = ""
                            sinup_city =""
                            sinup_accept = None
                         
                            messages.success(request,"your account is successfull")
                            is_add = True
                        else:
                            messages.error(request,'invalid email')
            else:
                messages.error(request,'you must agree to the terms')
        else:
            messages.error(request,"Check empty the field")
        return render(request,'account/sinup.html',{
            'fname':sinup_name,
            'femail':sinup_email,
            'fpassword':sinup_password,
            'faddress':sinpu_address,
            'fcity':sinup_city,
            'is_add':is_add
        })
    else:
        return render(request,'account/sinup.html')
def profile(request):
    if request.method =="POST" and 'btnprofile' in request.POST:
        if request.user is not None and request.user.id !=None:
            userprofiles = UserProfile.objects.get(user=request.user)
            if request.POST['username'] and request.POST['email'] and request.POST['password'] and request.POST['address'] and request.POST['city']:
                # request.user.username = request.POST['username']
                # request.user.email = request.POST['email']
                if not request.POST['password'].startswith('pbkdf2_sha256$'):
                    request.user.set_password(request.POST['password'])
                userprofiles.address = request.POST['address']
                userprofiles.city = request.POST['city']
                request.user.save()
                userprofiles.save()
                messages.success(request,'success profile')
                auth.login(request,request.user)
            else:
                messages.error(request,'chick the field is empty')  
       
        return redirect('profile')
    else:
        if request.user is not None:
            contex = None
            if not request.user.is_anonymous:
                userprofile = UserProfile.objects.get(user = request.user)
                contex = {
                    'name':request.user.username,
                    'email':request.user.email,
                    'password':request.user.password,
                    'address':userprofile.address,
                    'city':userprofile.city
                }
            return render(request,'account/profile.html',contex)
        else:
            return redirect('profile')
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('index')
#add the items in the favorit 
def favorit(request,pro_id):
    if  request.user.is_authenticated and not request.user.is_anonymous:
        pro_fav = product.objects.get(pk=pro_id)
        if UserProfile.objects.filter(user=request.user,product_favorit=pro_fav).exists():
            messages.success(request,'already product in the favorit list')
        else:
            userprofile = UserProfile.objects.get(user=request.user)
            userprofile.product_favorit.add(pro_fav)
            messages.success(request,'product hase been in the favorit')
    else:
        messages.error(request,'you must bee register ')
    return redirect('/product/')
#show the items in the favorit
def showfavorit(request):
    contex = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        userprofile = UserProfile.objects.get(user=request.user)
        userall = userprofile.product_favorit.all()
        cont={'pro':userall}
        return render(request,'product/detals/d/detals.html',cont)