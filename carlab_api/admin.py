# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Service, Category, SubCategory, User, Worker, Order

admin.site.register(Service)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(User)
admin.site.register(Worker)
admin.site.register(Order)

# Register your models here.
