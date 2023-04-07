from django import forms
from .models import Item


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'rear_image', )
        
        widgets = {
            'category': forms.Select(attrs={
               'class': 'form-control' 
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
             'rear_image': forms.FileInput( attrs={
                'class': 'form-control',
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'rear_image', 'is_sold',)
        
        widgets = {
            'category': forms.Select(attrs={
               'class': 'form-control' 
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
             'rear_image': forms.FileInput( attrs={
                'class': 'form-control',
            }),
        }
