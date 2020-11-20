from django.db import models
from django_countries.fields import CountryField


class Student(models.Model):

    ID = models.AutoField(primary_key = True)
    FirstName = models.CharField(max_length=40)
    MiddleName = models.CharField(max_length=40, blank=True)
    LastName = models.CharField(max_length=40)
    Email = models.CharField(max_length=30, blank=True)
    PhoneNumber = models.CharField(max_length=50)
    Status = models.IntegerField(default=1)
    UserSavedBy = models.IntegerField(default=0)
    StatusChangedBy = models.CharField(max_length=100)
    country = CountryField(multiple=True)

    def __str__(self):
        return self.FirstName + ' ' + self.LastName