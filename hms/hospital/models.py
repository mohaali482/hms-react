from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(_("First Name"), max_length=50)
    middle_name = models.CharField(_("Middle Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    b_date = models.DateField(_("Birth Date"), auto_now=False, auto_now_add=False)
    phone = models.PhoneNumberField(_("Phone"))
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


class PatientHistory(models.Model):
    patient = models.ForeignKey("Patient", verbose_name=_("Patient"), on_delete=models.CASCADE)
    conditons = models.ForeignKey("Condition", verbose_name=_("Condition"), on_delete=models.CASCADE)


