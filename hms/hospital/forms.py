from django import forms


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
    