from audioop import reverse
from gettext import ngettext
from pyexpat.errors import messages
from django.contrib import admin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from .models import Order,OrderDetails,JobOrderForm
from django_object_actions import DjangoObjectActions, action
from django.utils.html import format_html
from django.template.loader import get_template
from xhtml2pdf import pisa
import decimal, csv
import io
######################pdf import
from django.contrib import admin
from django.shortcuts import get_object_or_404
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame, KeepTogether
from reportlab.lib import colors
from django.http import HttpResponse
import audioop

# Your existing model and admin code...

##############################################
def download_pdf(self, request, queryset):
    # Assuming you have a template named 'pdf_template.html'
    template_path = 'your_template_for_job_order_form_pdf.html'
    
    # Render the template with the queryset data
    context = {'data': queryset}
    template = get_template(template_path)
    html = template.render(context)
    # Create a PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="output.pdf"'
    # Generate PDF using xhtml2pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # If PDF generation failed, return an error response
    if pisa_status.err:
        return HttpResponse("PDF generation error: {}".format(pisa_status.err))
    return response
download_pdf.short_description = "Download selected items as PDF"
########################################pdf

# Define a custom action for downloading PDF for JobOrderForm
@admin.action(description='Download csv')
def download_job_order_form_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/csv')
    response['Content-Disposition'] = 'attachment; filename="job_order_form.csv"'
    writer = csv.writer(response)
    orderjob = queryset.values_list('id','installationDate','installationTime','installationTime','note','numberproject','openingDate','openingTime','pdffile','proimg','projectManager','venueLocation')
    for ord in orderjob:
        writer.writerow(ord)
    return response
####################create pdf
def downloadpdf(self, request, queryset):
    model_name = self.model.__name__
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f"attachment;filename={model_name}.pdf"
    pdf = canvas.Canvas(response, pagesize=letter)
    pdf.setTitle('PDF Report')

    # Corrected line to get the fields
    headers = [field.verbose_name for field in self.model._meta.fields]
    data = [headers]
    for obj in queryset:
        data_row = [str(getattr(obj, field.name)) for field in self.model._meta.fields]
        data.append(data_row)

    table = Table(data)
    table.setStyle(TableStyle(
        [
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]
    ))
    canvas_width = 400
    canvas_height = 400
    table.wrapOn(pdf, canvas_width, canvas_height)
    table.drawOn(pdf, 30, canvas_height - len(data))
    pdf.save()
    return response

downloadpdf.short_description = "download pdf"
####################
    # template = get_template('your_template_for_job_order_form_pdf.html')
    # context = {'job_order_forms': queryset}
    # html = template.render(context)
    
    # # Create a PDF file
    # pisa_status = pisa.CreatePDF(html, dest=response)
    # if pisa_status.err:
    #     return HttpResponse('Error creating PDF', status=500)

    # return response

# Define a custom action for downloading PDF for Order
@admin.action(description='Download PDF for Order')
def download_order_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="order.pdf"'

    template = get_template('your_template_for_order_pdf.html')
    context = {'orders': queryset}
    html = template.render(context)

    # Create a PDF file
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error creating PDF', status=500)

    return response

# ... (your existing code)

##############################################
@admin.action(description='Make selected orders as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
    modeladmin.message_user(request, f'Successfully marked {queryset.count()} orders as published.')
    
class ReadOnlyAdmin(admin.TabularInline):
    model = OrderDetails
    extra = 0
    readonly_fields = ['get_user', 'get_order_date', 'get_is_finished','get_photo']
    def get_photo(self,obj):
        if obj.product.photo:
            return format_html(f"<img src='{obj.product.photo.url}'width='70'/>")
        return 'image not available'
    def get_user(self, instance):
        return instance.order.user

    def get_order_date(self, instance):
        return instance.order.order_date

    def get_is_finished(self, instance):
        return instance.order.is_finished

    get_user.short_description = 'img'
    get_user.short_description = 'المستخدم'
    get_order_date.short_description = 'Order Date'
    get_is_finished.short_description = 'Is Finished'

    def has_add_permission(self, request, obj=None):
        return False

class MyAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        # Filter the queryset based on the current user if needed
        queryset = super().get_queryset(request)
        return queryset
    list_display = ['id', 'clientName', 'date', 'jobOrderType', 'projectManager', 'handOverDateTime', 'get_photop', 'pdffile']
    def get_photop(self,obj):
        if obj.proimg:
            return format_html(f"<img src = '{obj.proimg.url}'width='60'/>")
        return 'the image not available'
    list_display_links = ['id', 'clientName']
    search_fields = ['numberproject','projectManager']
    date_hierarchy = 'date'
    actions = [download_pdf]
    # actions = [download_job_order_form_pdf,downloadpdf,download_pdf]


class OrderAdmin(admin.ModelAdmin):
    inlines = [ReadOnlyAdmin]
    list_display = ['id', 'jobordernumber', 'user',  'is_finished']
    actions = [make_published, download_order_pdf]   

admin.site.register(JobOrderForm, MyAdmin)
admin.site.register(Order, OrderAdmin)
