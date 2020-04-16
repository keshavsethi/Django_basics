from django import forms
from django.forms import ModelForm


from .models import *

class TasksForm(forms.ModelForm):
    name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    
    class Meta:
        model = Tasks
        fields = '__all__'
