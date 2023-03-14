from django.db import models


class Contact(models.Model):
    phone = models.CharField(max_length=20)
    adress = models.CharField(max_length=50)


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)