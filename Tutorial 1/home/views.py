from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse("This is home page")
    context = {
        'variable':"This is sent"
    }
    # messages.success(request, "This is a texst")
    return render(request, 'index.html', context)

def about(request):
    # return HttpResponse("This is about page")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("This is services page")
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse("This is contact page")
    if request.method == "POST":
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Address = request.POST.get('Address')
        Address_2 = request.POST.get('Address 2')
        State = request.POST.get('State')
        Zip = request.POST.get('Zip')
        # Cheak_me_out = request.POST.get('Cheak me out')
        contact = Contact(email=Email, passward=Password, Address=Address, Address2=Address_2, State=State, Zip_Code=Zip)
        contact.save()
        messages.success(request, "Profile Details Added Successfully")
    return render(request, 'contact.html')