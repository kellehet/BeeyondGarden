from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='services'),
    path('<str:service_type>', views.service, name='service'),

]