from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    phone = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.IntegerField()