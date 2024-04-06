from django import forms
from .models import JobOrderForm
class joborderforms(forms.ModelForm):
    class Meta:
        model = JobOrderForm
        fields = '__all__'