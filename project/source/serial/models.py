from django.db import models


class Guitar(models.Model):
    model = models.CharField(max_length=25, help_text='This is the model of the guitar')
    serial_number = models.CharField(max_length=15, help_text='Serial number input')
    year_of_purchase = models.IntegerField()
    brand_new = models.BooleanField()
    previous_owner = models.CharField(max_length=25)
    current_owner = models.CharField(max_length=25)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, null=True, blank=True)
    further_info = models.TextField()

