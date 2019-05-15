from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(name=name, email=email,phone=phone, message=message)
        contact.save()

        send_mail(
            'Beeyond Gardens Inquiry',
            'There has been an inquiry Beeyond Gardens',
            'kelleher.tyler90@gmail.com',
            [email, 'tyler_kelleher@hotmail.com'],
            fail_silently=False,
        )

        messages.success(request, 'Your request has been submitted. We will contact you soon')
    return redirect('/')