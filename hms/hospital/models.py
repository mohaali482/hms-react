from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(_("First Name"), max_length=50)
    middle_name = models.CharField(_("Middle Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    b_date = models.DateField(_("Birth Date"), auto_now=False, auto_now_add=False)
    phone = models.CharField(_("Phone number"), max_length=15)
    email = models.EmailField(_("Email"), max_length=254)
    sex = models.CharField(_("Sex"), max_length=10)
    blood_type = models.CharField(_("Blood Type"), max_length=2)

    def __str__(self) -> str:
        return self.email

    
class Condition(models.Model):
    symtopms = models.TextField(_("Symptopms"))
    condition = models.TextField(_("Conditions"))
    prescription = models.TextField(_("Prescription"))
    date = models.DateField(_("History Date"), auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.condition


class PatientHistory(models.Model):
    patient = models.ForeignKey("Patient", verbose_name=_("Patient"), on_delete=models.CASCADE)
    conditons = models.ForeignKey("Condition", verbose_name=_("Condition"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.patient + " " + self.conditons.date)


class Schedule(models.Model):
    date = models.DateTimeField(_("Entry date and time"), auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return str(self.date)


class EmployeeData(models.Model):
    user = models.ForeignKey("User", verbose_name=_("User"), on_delete=models.CASCADE)
    b_date = models.DateField(_("Birth Date"), auto_now=False, auto_now_add=False)
    phone_no = models.CharField(_("Phone Number"), max_length=15)
    sex = models.CharField(_("Sex"), max_length=10)
    role = models.CharField(_("Role"), max_length=20)
    schedule = models.ForeignKey("Schedule", verbose_name=_(""), on_delete=models.CASCADE)