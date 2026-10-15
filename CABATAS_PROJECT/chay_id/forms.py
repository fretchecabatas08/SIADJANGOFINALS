from django import forms
from .models import LostFoundItem


class LostFoundItemForm(forms.ModelForm):

    class Meta:
        model = LostFoundItem

        fields = [
            'item_name',
            'description',
            'category',
            'lost_found_status',
            'date_reported',
            'location',
            'color',
            'reporter_name',
            'contact_information',
            'item_status',
        ]

        widgets = {

            'item_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Black Wallet'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the item...',
                'rows': 4
            }),

            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Electronics, Personal Item'
            }),

            'lost_found_status': forms.Select(attrs={
                'class': 'form-control'
            }),

            'date_reported': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: School Library'
            }),

            'color': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: Black'
            }),

            'reporter_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),

            'contact_information': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email or phone number'
            }),

            'item_status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }