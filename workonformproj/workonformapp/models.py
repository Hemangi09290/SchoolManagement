from django.db import models
from pytz import country_names

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=15)

    def __str__(self):
        return self.country_name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.city_name

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    password = models.CharField(max_length=100, help_text='Enter 8 digits password')
    picture = models.ImageField()
    DOB = models.DateTimeField()
    email = models.EmailField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
        
    def __str__(self):
        return self.first_name


