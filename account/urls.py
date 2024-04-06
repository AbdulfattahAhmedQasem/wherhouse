from django.urls import path
from . import views
urlpatterns = [
    path('sinin',views.sinin,name='sinin'),
    path('sinup',views.sinup,name='sinup'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logout,name='logout'),
    path('favorit',views.favorit,name='favorit'),
    path('product_favorit/<int:pro_id>',views.favorit,name='product_favorit'),
    path('showproduct_favorit',views.showfavorit,name='showproduct_favorit'),
]
