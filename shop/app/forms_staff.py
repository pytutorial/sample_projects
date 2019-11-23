from django import forms
from .models import *

class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class CpuTypeForm(forms.ModelForm):
    class Meta:
        model = CpuType
        fields = '__all__'

class DiskTypeForm(forms.ModelForm):
    class Meta:
        model = DiskType
        fields = '__all__'

class ProductForm(forms.ModelForm):
    description = forms.CharField(max_length=500, label='Mô tả', required=False, widget=forms.Textarea)
    class Meta:
        model = Product
        fields = '__all__'        