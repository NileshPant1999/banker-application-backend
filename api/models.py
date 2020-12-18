from django.db import models

# Create your models here.
class BankDetails(models.Model):
    ifsc = models.CharField(max_length=60)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    bank_name = models.CharField(max_length=100, default="Central Bank Of India")

    def __str__(self):
        return self.ifsc