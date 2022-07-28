#from dataclasses import field
#from sqlite3.dbapi2 import _WindowAggregateClass
from django import forms
from .models import User
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserForm(forms.ModelForm):
    # phone_number = PhoneNumberField(
    #     widget = PhoneNumberPrefixWidget(initial='UZ')   
    # )

    class Meta():
        phone_number = PhoneNumberField(
        widget = PhoneNumberPrefixWidget(initial='UZ')   
        )
        model = User
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name:'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name:'}),
        }
