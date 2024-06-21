from django.db import models

class Item(models.Model):
    first_name = models.CharField(max_length=100, default='')
    middle_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=255, default='')
    email = models.EmailField(default='')  
    phone_no = models.CharField(max_length=20, default='')

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

