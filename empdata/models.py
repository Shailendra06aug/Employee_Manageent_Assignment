
from django.db import models

# Create your models here.

class EmployeeInfo(models.Model):
  
  sl_id = models.AutoField(primary_key= True) 
  company_name= models.CharField(max_length=100, default="")
  role= models.CharField(max_length=50, default="")
  date_of_join =  models.DateField()
  last_date =     models.DateField(default='Test',null=True,blank=True)
  
  def __str__(self):
    return self.company_name
 
