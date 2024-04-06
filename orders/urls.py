from django.urls import path

from orders.admin import download_pdf
from . import views

#create array containt all page 
urlpatterns = [
    path('add_to_car/<int:pro_id>',views.add_to_cart,name='add_to_cart'),
    path('showCart',views.showCart,name='showCart'),
    path('remov_product/<int:orderdetalsid>',views.delete_cart,name="delete_cart"),
    path('add_qty/<int:orderdetalsid>',views.add_qty,name="add_qty"),
    path('sub_qty/<int:orderdetalsid>',views.sub_qtu,name='sub_qty'),
    path('pyment',views.pyment,name='pyment'),
    path("show_order",views.show_orders,name='show_order'),
    path('shownumberjob',views.shownumberjob,name='shownumberjob'),
    path('jobOrderFrom',views.joborder,name='jobOrderFrom'),
    # path('pdf',views.render_pdf_view,name='pdf'),

    # path('pdf/<int:pk>/',views.custom_pdf_view,name='customer-pdf-view')
    # path('joborder',views.jobOrderForm)       
]