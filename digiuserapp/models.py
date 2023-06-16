from django.db import models

# Create your from django.db import models

#  Create your models here.
class Userlogdb(models.Model):
     User_Name = models.CharField(max_length=100, null=True, blank=True)
     Email=models.EmailField(max_length=100,null=True,blank=True)
     Mobile_Number=models.IntegerField(null=True,blank=True)
     Password=models.CharField(max_length=100,null=True,blank=True)
     Image=models.ImageField(upload_to="userimg",null=True,blank=True)

class cartdb(models.Model):
     User_Name=models.CharField(max_length=100,null=True,blank=True)
     Product_Name=models.CharField(max_length=100,null=True,blank=True)
     Description=models.CharField(max_length=100,null=True,blank=True)
     Quantity=models.CharField(max_length=100,null=True,blank=True)
     Price=models.IntegerField(null=True,blank=True)
     Total_price=models.IntegerField(null=True,blank=True)

class checkoutDb(models.Model):
     First_name=models.CharField(max_length=100,null=True,blank=True)
     Last_name=models.CharField(max_length=100,null=True,blank=True)
     User_name=models.CharField(max_length=100,null=True,blank=True)
     Email=models.EmailField(max_length=100,null=True,blank=True)
     Address1=models.CharField(max_length=100,null=True,blank=True)
     Address2=models.CharField(max_length=100,null=True,blank=True)
     Country=models.CharField(max_length=100,null=True,blank=True)
     State=models.CharField(max_length=100,null=True,blank=True)
     Zip=models.IntegerField(null=True,blank=True)
     payment=models.CharField(max_length=100,null=True,blank=True)
     Name_on_card=models.CharField(max_length=100,null=True,blank=True)
     credi_card_number=models.IntegerField(null=True,blank=True)
     Expire_date=models.IntegerField(null=True,blank=True)
     Cvv=models.IntegerField(null=True,blank=True)



     



