#  ##########################
    
#     def downloadpdf(self, request, queryset):
#         model_name = self.model.__name__
#         buffer = io.BytesIO()

#         # Create PDF document
#         pdf = SimpleDocTemplate(buffer, pagesize=letter)

#         # Configure styles
#         styles = getSampleStyleSheet()
#         styles['Title'].fontName = 'Helvetica-Bold'
#         styles['Normal'].fontSize = 10

#         # Table data, headers, and rows
#         headers = [field.verbose_name for field in self.model._meta.fields]
#         data = [headers]
#         for obj in queryset:
#             data_row = [str(getattr(obj, field.name)) for field in self.model._meta.fields]
#             data.append(data_row)

#         # Create table and style
#         table = Table(data, repeatRows=1, hAlign='CENTER', style=TableStyle(
#             [
#                 ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
#                 ('GRID', (0, 0), (-1, -1), 1, colors.black),
#                 ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
#                 ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
#                 ('FONTSIZE', (0, 0), (-1, -1), 10),
#                 ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#                 ('BACKGROUND', (0, 1), (-1, -1), colors.white),
#                 ('GRID', (0, 1), (-1, -1), 1, colors.black),
#                 ('LEFTPADDING', (0, 0), (-1, -1), 5),
#                 ('RIGHTPADDING', (0, 0), (-1, -1), 5),
#             ]
#         ))

#         # Build the PDF document
#         content = []

#         # Header
#         header_text = f"{model_name} Report"
#         header_style = ParagraphStyle('Header', parent=styles['Title'], fontSize=10)
#         header = Paragraph(header_text, header_style)
#         content.append(header)

#         # Spacer
#         content.append(Spacer(1, 5))

#         # Table
#         content.append(table)

#         # Build the PDF document
#         pdf.build(content)

#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = f"attachment;filename={model_name}.pdf"
#         response.write(buffer.getvalue())
#         return response

#     downloadpdf.short_description = "Download PDF"
#     ##########################