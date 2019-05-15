from django.shortcuts import render
from services.models import Service

# Create your views here.
def index(request):
    services = Service.objects.all()
    context = {
        'services': services
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')