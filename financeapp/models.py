from django.db import models

# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.fullname

class LogInForm(models.Model):
    fullname = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)

    def __str__(self):
        return self.fullname


class appointment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.name






