# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=60)
    image = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return 'Service: ' + self.name

    def __getitem__(self, key):
        return self.service[key]

# Category Model
class Category(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    price = models.FloatField()
    sub_cat = models.BooleanField()
    duration = models.IntegerField()
    image = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categories"

    def __unicode__(self):
        return 'Category: ' + self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=60)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "sub categories"


# User Model
class User(models.Model):
    fireID = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return  self.name



class Worker(models.Model):
    fireID = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    status = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

#Order Model
class Order(models.Model):
    service = models.CharField(max_length=100)
    cat_name = models.CharField(max_length=100)
    worker =  models.CharField(max_length=100)
    user =  models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    comments = models.TextField()
    ammount = models.CharField(max_length=30)
    car_plate = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    service_date = models.DateTimeField()

    def __unicode__(self):
        return  self.name

class Schedule(models.Model):
    order_id = models.CharField(max_length=100)
    reserved_date = models.DateTimeField()

    def __unicode__(self):
        return  self.name


class UserPlate(models.Model):
    user_id = models.CharField(max_length=100)
    number = models.CharField(max_length=50)

    def __unicode__(self):
        return  self.name

class UserBilling(models.Model):
    user_id = models.CharField(max_length=100)
