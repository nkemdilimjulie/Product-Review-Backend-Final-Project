from django.db import models
from django.core.validators import RegexValidator

#Create your models here.

# This model to be used by Admin user only to create mobile phones entries in database 
class Mobiles(models.Model):
    ean = models.CharField(
        max_length=13, primary_key=True, 
        validators=[RegexValidator(regex=r'^\d{13}$', message="EAN must be exactly 13 digits.")],
        help_text="Enter a 13-digit EAN (only numbers)."
    ) # primary key, barcode length of 13 digits
    brand = models.CharField(max_length=50, blank=False, null=False)
    model = models.CharField(max_length=50,  blank=False, null=False)
    description = models.TextField(max_length=500,  blank=False, null=False)

