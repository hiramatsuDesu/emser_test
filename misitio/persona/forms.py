from django import forms
from .models import Persona
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    mail = forms.EmailField(max_length=100)
    

class PersonaModelForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'mail', 'id']

    def __init__(self, *args, **kwargs):
        super(PersonaModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar'))