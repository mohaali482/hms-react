from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from .models import *


GenderChoices = [("",""),("Female","Female"), ("Male","Male") ]
BloodTypes = [("",""),("A+","A+" ), ("A-", "A-"), ("B-","B-"),("B+", "B+"),("AB+","AB+"), ("AB-","AB-"),("O-","O-"),("O+", "O+")]

class RegisterPatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(RegisterPatientForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


    class Meta :
        model = Patient
        fields = ("first_name" , "middle_name" , "last_name", "phone" , "b_date" , "email" , "sex" , "blood_type",)
        # sex = forms.ChoiceField(label = "Sex", choices=[GenderChoices ], required=True, widget=forms.Select(choices=(GenderChoices)))
        # blood_type = forms.ChoiceField( label = "Blood Type",choices=[BloodTypes], required=False)

        widgets = {
            'sex': forms.Select(choices=(GenderChoices),attrs={'class':'form-control custom-select'}),
            'blood_type': forms.Select(choices = (BloodTypes),attrs={'class':'form-control custom-select'}),
            'b_date':forms.TextInput(attrs={'type':"date", 'class':"form-control"})
        }
        


class RegisterPatientCondition(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(RegisterPatientCondition, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta :
        model = Condition
        fields = ["symtopms", "condition", "prescription"]


class EditPatient(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(EditPatient, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta :
        model = Patient
        fields = [
        'first_name',
        'middle_name',
        'last_name',
        'email',
        'phone',
<<<<<<< HEAD
        ]
=======
        ]


# class RegisterEmployeeData(forms.ModelForm):
#     def __init__(self, *args, **kwargs) -> None:
#         super(RegisterEmployeeData, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'

#     class Meta :
#         model = EmployeeData
#         fields = ["Fname", "condition", "prescription"]

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


>>>>>>> 6cfe1e772fb64e16280da08a42ca08234a2a4cd7
