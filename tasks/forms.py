from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title'] #tylko pole do pokazania

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 
            'placeholder': 'Wpisz nowe zadanie....'})
        }