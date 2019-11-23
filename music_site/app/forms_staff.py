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

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

    description = forms.CharField(required=False, label='Mô tả', widget=forms.Textarea)