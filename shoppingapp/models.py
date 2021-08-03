from django.db import models
# Create your models here.
class product(models.Model):
    pname = models.CharField(max_length=100)
    pdisc = models.TextField()
    pabout = models.TextField()
    pprice = models.FloatField()
    pimg1 = models.ImageField(upload_to='pics')
    pimg2 = models.ImageField(upload_to='pics')
    pimg3 = models.ImageField(upload_to='pics')
    status = models.BooleanField(default=False)
    count = models.IntegerField()
    code = models.CharField(max_length=100)
    poffer = models.FloatField()
    paylink=models.CharField(max_length=300)
class user(models.Model):
	uname = models.CharField(max_length=100)
	umail = models.EmailField(max_length=100)
	usubject = models.CharField(max_length=100)
	umessage = models.TextField(max_length=200)
class shoppingdetails(models.Model):
    uname = models.CharField(max_length=100)
    uHname = models.CharField(max_length=100)
    uemail = models.EmailField(max_length=100)
    umob = models.CharField(max_length=15)
    upostoffice = models.CharField(max_length=200)
    ulandmark = models.CharField(max_length=200)
    upin = models.IntegerField()
    ucity = models.CharField(max_length=200)
    udistrict = models.CharField(max_length=100)
    ustate = models.CharField(max_length=100)
    ucountry = models.CharField(max_length=100)
    quantity = models.IntegerField()
    pid = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    price = models.FloatField()
    code= models.CharField(max_length=100)
    delivery=models.BooleanField(default=False)
    tracking=models.CharField(max_length=200)
class reviewdetails(models.Model):
    customercode = models.CharField(max_length=20)
    customername = models.CharField(max_length=100)
    customermessage = models.TextField(max_length=200)
    status = models.BooleanField(default=False)




