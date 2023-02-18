from django import forms
from .models import ToDo

class ToDoForm(forms.ModelForm):

    tasks=forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Add new task..."}))


    class Meta:
        model= ToDo
        fields="__all__"

