from django import forms
from django.forms import fields
from .models import Todo
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
    text = forms.CharField(max_length=900, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Write your todo', 'aria-describedby' : 'button-addon2', 'id' : 'floatingInput'}))
    