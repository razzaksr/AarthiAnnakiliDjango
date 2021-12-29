from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Forum(models.Model):
    name=models.CharField(max_length=250)
    technology=models.CharField(max_length=250)
    head=models.CharField(max_length=250)
    members=models.IntegerField(null=True)
    hours=models.IntegerField()
    
    class Meta:
        db_table='forum'