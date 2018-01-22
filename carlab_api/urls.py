from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^get_services/$', views.services , name = "services"),
    url(r'^service_categories/(?P<service_id>[0-9]*)/', views.get_categories, name = "service_categories"),
    url(r'^new_order/$', views.createOrder, name = "new_order"),
    url(r'^create_worker/$', views.createWorker, name = "new_worker"),
    url(r'^worker_status/$', views.workerStatus, name = "worker_status"),
    url(r'^get_worker/$', views.getWorker, name = "get_worker"),
    url(r'^done_order/$', views.doneOrder, name = "done_order")

]
