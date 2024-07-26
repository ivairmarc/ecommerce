from django import forms
from website.models import Employees


class EmployModelForm(forms.ModelForm):

    class Meta:
        model = Employees
        fields = '__all__'