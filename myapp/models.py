from django.db import models

# Create your models here.
class couplemodel(models.Model):

    Bfname=models.CharField(max_length=50)
    Gfname=models.CharField(max_length=50)
    probofmarr=models.IntegerField()
    

    