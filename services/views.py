
from django.shortcuts import render, get_object_or_404
from .models import Service


# Create your views here.

def service(request, service_type):
    service = get_object_or_404(Service, pk=service_type)
    services = Service.objects.all()



    context = {
        'service':  service,
        'services': services
    }
    return render(request, 'services/service.html', context)

