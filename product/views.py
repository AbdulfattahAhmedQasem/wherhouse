from audioop import reverse
from decimal import Decimal, InvalidOperation
from django.shortcuts import get_object_or_404, render
from .models import product,category, yourmodels,modelNotices  # Replace with the correct import statement for your Product model
from .fo import ExcelUploadForm
import pandas as pd
from django.db.models import Q

def index(request):
    name = None
    if 'searchname' in request.GET:
        name = request.GET['searchname']
    cont = {
        'prohome':category.objects.all(),
        'names':name,
        'notimg':modelNotices.objects.all()
    }
    return render(request,'product/home.html',cont)
def tables(request, pro_id):
    context = {
         'pro': product.objects.filter(categorys_id=pro_id),
         'cat':get_object_or_404(category,id= pro_id),
    }
    return render(request, 'product/table.html', context)
def screen(request):
    context = {
        'pro':product.objects.all()
    }
    return render(request,'product/table.html',context)
def sound(request, pro_id):
    context = {
        'pro':get_object_or_404(product,id=pro_id)
    }
    return render(request,'product/sound.html',context)
################################
def showprodetails(request,det_id):
    context = None
    context = {
        'pro':get_object_or_404(product,pk=det_id)
    }
    return render(request,'product/detals/productdetails.html',context)
################################
def detals(request):
    pro = product.objects.all()
    name = None
    typees= None
    shape = None
    height = None
    id=None
    filter_conditions = Q()
    search_term = request.GET.get('searchname', None)
    if search_term:
        try:
            search_number = Decimal(search_term)
        except InvalidOperation:
            search_number = None

        filter_conditions |=Q(name__icontains=search_term) |Q(shapeproduct__icontains=search_term)

        # Check if search_number is not None before adding numeric conditions
        if search_number is not None:
            filter_conditions |= Q(productlength=search_number) | Q(productwidth=search_number) | Q(id=search_number)

        # Apply the filter conditions to the queryset
        pro = pro.filter(filter_conditions)

    cont = {'pro': pro}
    return render(request,'product/detals/d/detals.html',cont)
########################################################form import
def import_from_excel(request):
    # يتحقق من ان النموذج مرسل 
    if request.method == 'POST':
        # generate the form
        form = ExcelUploadForm(request.POST, request.FILES)
        #chick the form is availabel
        if form.is_valid():
            #reade the data from axcel to the excel_data variable
            excel_data = pd.read_excel(request.FILES['file'])
            #conver the 
            data_list = excel_data.to_dict(orient='records')
            yourmodels.objects.bulk_create([yourmodels(**data) for data in data_list])

    else:
        form = ExcelUploadForm()

    return render(request, 'product/import_from_excel.html', {'form': form})

