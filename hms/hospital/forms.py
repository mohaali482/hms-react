from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields

from .models import *


GenderChoices = [("Female","Female"), ("Male","Male") ]
BloodTypes = [("A+","A+" ), ("A-", "A-"), ("B-","B-"),("B+", "B+"),("AB+","AB+"), ("AB-","AB-"),("O-","O-"),("O+", "O+")]

class RegisterPatientForm(forms.ModelForm):

    class Meta :
        model = Patient
        fields = ("first_name" , "middle_name" , "last_name", "phone" , "b_date" , "email" , "sex" , "blood_type",)

        first_name = forms.CharField(label = "First Name",max_length=20, min_length=2, required=True, widget=forms.TextInput(attrs={
        'type':'name',
        'placeholder':'First Name'
        }))
        middle_name = forms.CharField(label = "Middle Name",max_length=20, min_length=2, required=True, widget=forms.TextInput(attrs={
            'type':'name',
            'placeholder':'Middle Name'
        }))
        last_name = forms.CharField(label = "Last Name",max_length=20, min_length=2, required=True, widget=forms.TextInput(attrs={
            'type':'name',
            'placeholder':'Last Name'
        }))
        phone = forms.CharField(label = "Phone Number", max_length=13, required=True, min_length=2 , widget=forms.TextInput(attrs={
            'type':'number',
            'placeholder':'Phone number'
        }))
        b_date = forms.DateField(label = "Birth Date",required= True)
        email = forms.EmailField(label = "Email",required= False,  widget=forms.TextInput(attrs={
            'type':'email',
            'placeholder':'Email'
        }))
        sex = forms.ChoiceField(label = "Sex", choices=[GenderChoices ], required=True)
        blood_type = forms.ChoiceField( label = "Blood Type",choices=[BloodTypes], required=False)
        


# class RegisterPatientCondition(forms.ModelForm):

#     symtopms = forms.CharField(min_length=2, required=True, widget=forms.TextInput(attrs={
#         'type':'char',
#         'placeholder':'Symtopms'
#     }))
#     Condition = forms.CharField(min_length=2, required=True, widget=forms.TextInput(attrs={
#         'type':'char',
#         'placeholder':'Conditions'
#     }))
#     prescription = forms.CharField(min_length=2, required=True, widget=forms.TextInput(attrs={
#         'type':'char',
#         'placeholder':'Prescription'
#     }))
#     date =  forms.DateTimeField(auto_now = True, auto_now_add = True )
#     class Meta :
#         model = Condition
#         fields = ["symtopms", "condition", "prescription", "date"]

# class RegisterEmployeeData(forms.ModelForm):
    
#     User = forms.ModelChoiceField()
#     b_date = forms.DateField()
#     phone_no = forms.forms.CharField( max_length=13, required=True, min_length=2 , widget=forms.TextInput(attrs={
#         'type':'number',
#         'placeholder':'Phone Number'
#     }))
#     sex = forms.ChoiceField( choices=[GenderChoices ], required=True)
#     role = forms.forms.CharField( min_length = 2 ,max_length=20, required= True )
#     schedule = forms.ModelChoiceField()
#     class Meta :
#         model = EmployeeData
#         fields = ["user", "b_date", "phone_no", "sex", "role", "schedule"]