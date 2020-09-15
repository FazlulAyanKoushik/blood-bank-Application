from django.db import models

# Create your models here.
class BloodDonor(models.Model):
    donor_id = models.CharField(max_length = 20)
    donor_name = models.CharField(max_length = 100)
    donor_blood_group = models.CharField(max_length = 20)
    donor_email = models.EmailField(blank = True, null = True)
    donor_contact = models.CharField(max_length = 11)
    