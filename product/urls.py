from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:pro_id>',views.tables,name="tables"),
    # path('screens',views.screen,name='screens'),
    path('detals',views.detals,name='detals'),
    path('import/', views.import_from_excel, name='import_from_excel'),
    path('showdetails/<int:det_id>',views.showprodetails,name='showdetails'), 
   
]
