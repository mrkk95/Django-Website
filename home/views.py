from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is homepage")


def about(request):
    #return HttpResponse("This is about page")
    return render(request, 'about.html')


def services(request):
    #return HttpResponse("This is services page")
    return render(request, 'services.html')


def contact(request):
    if(request.method == "POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        msg=request.POST.get('msg')  
        contact=Contact(name=name,email=email,phone=phone,msg=msg)
        contact.save()
        messages.success(request, 'Details has been sent to the owner of this site!')
    return render(request, 'contact.html')