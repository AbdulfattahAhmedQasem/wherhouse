# forms.py
# مكتبة تستخدم لانشاء نماذج ويب 
from django import forms
class ExcelUploadForm(forms.Form): # لانشاء نموذج ويب
    # اسم الحقل الذي من خلالة سيتم تحميل ملف الاكسل الية 
    file = forms.FileField()
