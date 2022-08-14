from cgi import print_exception
import email
from sre_constants import CATEGORY
from statistics import mode
from telnetlib import STATUS
from unicodedata import category, name
from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=190, null=True)
    email = models.CharField(max_length=190, null=True)
    phone = models.CharField(max_length=190, null=True)
    age = models.IntegerField(null=True)
    deta_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name + self.email


class Tag(models.Model):
    name = models.CharField(max_length=190, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    CATEGORY = (
        ('Classics', 'Classics'),
        ('Comic Book', 'Comic Book'),
        ('Fantasy', 'Fantasy'),
        ('Horror', 'Horror')
    )
    name = models.CharField(max_length=190, null=True)
    authoname = models.FloatField(max_length=190, null=True)
    price = models.CharField(max_length=190, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    tag = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('Delivered', 'Deliverd'),
        ('in progress', 'in progress'),
        ('out of order', 'out of order')

    )
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
