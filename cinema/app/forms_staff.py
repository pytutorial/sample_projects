from django import forms
from .models import *

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class MovieForm(forms.ModelForm):
    description = forms.CharField(required=False, label='Mô tả', widget=forms.Textarea)
    onDate = forms.DateField(label='Ngày khởi chiếu', input_formats=['%d/%m/%Y'],
                    widget=forms.DateInput(format = '%d/%m/%Y'))
    
    class Meta:
        model = Movie
        fields = '__all__' 

class MovieShowForm(forms.ModelForm):
    class Meta:
        model = MovieShow
        fields = '__all__' 
