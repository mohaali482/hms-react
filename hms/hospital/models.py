from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(_("First Name"), max_length=50)
    middle_name = models.CharField(_("Middle Name"), max_length=50,blank=True, null= True)
    last_name = models.CharField(_("Last Name"), max_length=50)
    b_date = models.DateField(_("Birth Date"), auto_now=False, auto_now_add=False)
    phone = models.CharField(_("Phone number"), max_length=15)
    email = models.EmailField(_("Email"), max_length=254, blank=True, null=True)
    sex = models.CharField(_("Sex"), max_length=10)
    blood_type = models.CharField(_("Blood Type"), max_length=2, blank=True, null=True)

    def __str__(self) -> str:
        if self.email:
            return self.email
        else:
            return f'Phone : {self.phone}'
    
    def full_name(self) -> str:
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"

        else:
            return f"{self.first_name} {self.last_name}"

    
class Condition(models.Model):
    symtopms = models.TextField(_("Symptopms"))
    condition = models.TextField(_("Conditions"))
    prescription = models.TextField(_("Prescription"))
    date = models.DateField(_("History Date"), default=timezone.now, blank=True, null=True)

    def __str__(self) -> str:
        return self.condition


class PatientHistory(models.Model):
    patient = models.ForeignKey("Patient", verbose_name=_("Patient"), on_delete=models.CASCADE)
    conditions = models.ForeignKey("Condition", verbose_name=_("Condition"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.patient.first_name + " " + str(self.conditions.date))

    def condition_name(self) -> str:
        return str(self.conditions.condition)


class Schedule(models.Model):
    date = models.DateTimeField(_("Entry date and time"), auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return str(self.date)


class EmployeeData(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name='employee')
    b_date = models.DateField(_("Birth Date"), auto_now=False, auto_now_add=False)
    phone_no = models.CharField(_("Phone Number"), max_length=15)
    sex = models.CharField(_("Sex"), max_length=10)
    role = models.CharField(_("Role"), max_length=20)
    schedule = models.ForeignKey("Schedule", verbose_name=_("Schedule"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.user.username)


class Queue(models.Model):
    patient = models.ForeignKey("Patient", verbose_name=_("Patient"), on_delete=models.CASCADE, related_name='patient')

    def __str__(self):
        return self.patient.first_name

    def get_patient(self) -> Patient:
        return self.patient
    