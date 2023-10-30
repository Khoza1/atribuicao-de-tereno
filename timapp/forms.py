from django import forms
from .models import Terreno, RecursoNatural, Documento

class TerrenoForm(forms.ModelForm):
    class Meta:
        model = Terreno
        fields = '__all__'

class RecursoNaturalForm(forms.ModelForm):
    class Meta:
        model = RecursoNatural
        fields = '__all__'

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'
