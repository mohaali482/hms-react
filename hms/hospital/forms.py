from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from .models import *


#created the needed forms for the system 



# created an array to hold  Gender and bloodtype choices  
GenderChoices = [("",""),("Female","Female"), ("Male","Male") ]
BloodTypes = [("",""),("A+","A+" ), ("A-", "A-"), ("B-","B-"),("B+", "B+"),("AB+","AB+"), ("AB-","AB-"),("O-","O-"),("O+", "O+")]



# patient register form
class RegisterPatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(RegisterPatientForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    class Meta :
        model = Patient
        fields = ("first_name" , "middle_name" , "last_name", "phone" , "b_date" , "email" , "sex" , "blood_type",)

        widgets = {
            'sex': forms.Select(choices=(GenderChoices),attrs={'class':'form-control custom-select'}),
            'blood_type': forms.Select(choices = (BloodTypes),attrs={'class':'form-control custom-select'}),
            'b_date':forms.TextInput(attrs={'type':"date", 'class':"form-control"})
        }



# register patient condition form  

class RegisterPatientCondition(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(RegisterPatientCondition, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta :
        model = Condition
        fields = ["symtopms", "condition", "prescription"]



# edit patient form  

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
        ]



# condition update form 
class ConditionUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(ConditionUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    

    class Meta:
        model = Condition
        fields = [
            'symtopms',
            'condition',
            'prescription'
        ]

# class RegisterEmployeeData(forms.ModelForm):
#     def __init__(self, *args, **kwargs) -> None:
#         super(RegisterEmployeeData, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'

#     class Meta :
#         model = EmployeeData
#         fields = ["user", "b_date", "phone_no", sex , "role" , "schedule" ]



# created user register form 
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# creating Edit profile form for our user 
class UpdateProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


