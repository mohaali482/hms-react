from django import forms
from django.db import models


GenderChoices = [("Female","Female"), ("Male","Male") ]
BloodTypes = [("A+","A+" ), ("A-", "A-"), ("B-","B-"),("B+", "B+"),("AB+","AB+"), ("AB-","AB-"),("O-","O-"),("O+", "O+")]

class RegisterPatientForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20, min_length=2, required=True, widget=forms.TextInput(attrs={
        'type':'name',
        'placeholder':'First Name'
    }))
    middle_name = forms.CharField(max_length=20, min_length=2, required=True, widget=forms.TextInput(attrs={
        'type':'name',
        'placeholder':'Middle Name'
    }))
    last_name = forms.CharField(max_length=20, min_length=2, required=True, widget=forms.TextInput(attrs={
        'type':'name',
        'placeholder':'Last Name'
    }))
    phone = forms.forms.CharField( max_length=13, required=True, min_length=2 , widget=forms.TextInput(attrs={
        'type':'number',
        'placeholder':'Phone number'
    }))
    b_date = forms.DateField(required= True)
    email = forms.EmailField(required= False,  widget=forms.TextInput(attrs={
        'type':'email',
        'placeholder':'Email'
    }))
    sex = forms.ChoiceField( choices=[GenderChoices ], required=True)
    blood_type = forms.ChoiceField( choices=[BloodTypes], required=False)
class RegisterPatientCondition(forms.ModelForm):
     symtopms = forms.