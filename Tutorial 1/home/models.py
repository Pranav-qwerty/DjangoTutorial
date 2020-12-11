from django.db import models

# Create your models here.
class Contact(models.Model):
    """
    docstring
    """
    email = models.CharField(max_length=122)
    passward = models.CharField(max_length=50)
    Address = models.CharField(max_length=300)
    Address2 = models.CharField(max_length=300)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=50)
    Zip_Code = models.CharField(max_length=5)
    def __str__(self):
        return self.email
    
    