# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Service, Category, Worker, Order, SubCategory
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import *
from django.forms.models import model_to_dict
from pusher import Pusher
from django.forms.models import model_to_dict
import json

# Pusher Data.
pusher = Pusher(  app_id=u'457719',  key=u'1f8d9c19abfb2a61a064',  secret=u'd143b896c5f8715af3c0',  cluster=u'us2',  ssl=True)

# Create your views here.
@require_GET
def services(request):
    data = Service.objects.all().values()
    return JsonResponse({
    'data': list(data)
    })
    # return HttpResponse(content=list(data), content_type="application/json",status=200)

@require_GET
def get_categories(request, service_id):

    subcategories = []
    categories = Category.objects.filter(service_id = service_id).values('name', 'price', 'duration', 'id', 'image', 'sub_cat')

    for category in categories:

        if category['sub_cat'] != False:
            sub_category = getSubCategories(category['id'])

        else:



    return JsonResponse({
    'category': list(data),
    'sub_categories': list(sub_category)
    })

    return JsonResponse({
    'category': list(data),
    })


    # return HttpResponse(content=list(data), content_type="application/json",status=200)

@require_GET
def createOrder(request):
    message = " "
    pusher.trigger('orders', 'new-order', {message: "Order Arrived"})
    return HttpResponse()

@csrf_exempt
def createWorker(request):
    data = json.loads(request.body.decode('utf-8'))

    worker = Worker(fireID = data['fireID'], name= data['name'], last_name = data['last_name'], email= data['email'], role= data['role'], status= 'off_duty', phone= data['phone'])

    worker.save()
    pusher.trigger('orders', 'new-order', {model_to_dict(worker)})
    return HttpResponse();

@csrf_exempt
def getWorker(request):
    data = json.loads(request.body.decode('utf-8'))
    print data
    worker = model_to_dict(Worker.objects.get(fireID = data['fireID']))
    workerID = data['fireID']
    role = worker['role']

    orders = getWorkerOrders(workerID, role)

    return JsonResponse({
    'worker': worker
    })

@csrf_exempt
def getOrders(request):
    data = json.loads(request.body.decode('utf-8'))

    orders = Order.objects.filter(worker = data['worker']).values('name', 'status', 'latitude', 'longitude', 'cat_name')

    return JsonResponse({
    'data': list(orders)

    })

@csrf_exempt
def workerStatus(request):
    data = json.loads(request.body.decode('utf-8'))

    worker = model_to_dict(Worker.objects.get(fireID = data['fireID']))
    worker_id = data['fireID']

    if worker['status'] != 'on_dutty':
        Worker.objects.filter(fireID = worker_id).update( status = 'on_dutty' )
    else:
        Worker.objects.filter(fireID = worker_id).update( status = 'off_dutty' )


    new_status = model_to_dict( Worker.objects.get(fireID = data['fireID']) )

    return JsonResponse({
    'data': new_status['status']
    })

@csrf_exempt
def doneOrder(request):
    data = json.loads(request.body.decode('utf-8'))

    order_id = data['id']

    if order_id != 'terminada':
        Order.objects.filter(id=order_id).update(status='terminada')
    else:
        Order.objects.filter(fireID=worker_id).update(status='off_dutty')

    new_status = Order.objects.filter(id=order_id).values(status)
    return JsonResponse({
    'data': list(order_id)
    })

#Custom Reusable Functions<------------------------------------------------------------------------>

#<!-- Fetch Orders By Worker ID -->
def getWorkerOrders(workerID, role):

    orders = model_to_dict( Order.objects.get( worker = workerID, status = "active", service = role ) )

    return orders

#<!-- Fetch SubCategory By Category ID -->
def getSubCategories( category_id ):

    sub_categories = model_to_dict( SubCategory.objects.get( category_id = category_id ) )

    return sub_categories

#<!------------------------------------------------------------------------------------------------>
