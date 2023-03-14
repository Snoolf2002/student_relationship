from django.db import models


class Contact(models.Model):
    phone = models.CharField(max_length=20)
    adress = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.phone


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.first_name