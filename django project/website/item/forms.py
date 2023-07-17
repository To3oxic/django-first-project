from django import forms

from .models import Catagory,Item

INPUT_CLASSES = 'w-full px-6 py-4 rounded-xl'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category','name','description','price','image')
        widgets = {
                'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
                }),
                'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                }),
                'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                }),
                'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                }),
                'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
                }),
                
            }