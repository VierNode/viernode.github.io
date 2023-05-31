from django.db import models
from datetime import datetime

class pricing_table(models.Model):
    package_name = models.CharField( max_length=50)
    package_amount = models.CharField( max_length=50)
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=50)
    number = models.CharField( max_length=50)
    password = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)
    

    def __str__(self):
        return self.name +" - "+ self.package_name +" - "+ self.package_amount
    
class membership (models.Model):
    name = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    number = models.CharField( max_length=50)
    message = models.CharField( max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.name +" - "+self.email+" - "+self.number

class contact_us (models.Model):
    name = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    number = models.CharField( max_length=50)
    message = models.CharField( max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.name +" - "+self.email+" - "+self.number
    
class newsletter (models.Model):
    
    email = models.CharField( max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.email
    
class login_details (models.Model):
    username=models.CharField( max_length=50)
    password = models.CharField( max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.username
    
    

    
    
    






    

