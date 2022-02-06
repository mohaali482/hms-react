from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from .models import *


# In forms here we created the form we needed for our system 



# we made Gender choices and bloodtype a choice fields 
GenderChoices = [("",""),("Female","Female"), ("Male","Male") ]
BloodTypes = [("",""),("A+","A+" ), ("A-", "A-"), ("B-","B-"),("B+", "B+"),("AB+","AB+"), ("AB-","AB-"),("O-","O-"),("O+", "O+")]



# we our register form for our patient and used the data we got in our models as fields

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



# we creating a patient condition form from our models and make them fields here

class RegisterPatientCondition(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(RegisterPatientCondition, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta :
        model = Condition
        fields = ["symtopms", "condition", "prescription"]



# we are creating a patient info edit form here 

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



# we created user register form 
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# we creating Edit profile form for our user 
class UpdateProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


