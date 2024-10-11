#from django.db import models

# Create your models here.

from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  email = models.EmailField(null=True)
  joined_date = models.DateField(null=True)
  

  def _str_(self):
    return f'{self.firstname} {self.lastname}'