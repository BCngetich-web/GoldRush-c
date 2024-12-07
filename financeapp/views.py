from django.shortcuts import render , redirect
from financeapp.models import appointment
from financeapp.models import Contact

# Create your views here.

def index(request):
    return render(request,'index.html')

def portfolio(request):
    return render(request,'portfolio-details.html')

def services(request):
    return render(request,'service-details.html')

def starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        contactdetails=Contact(
            name  = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],

        )
        contactdetails.save()
        return redirect('/about')

    else:
        return render(request, 'contact.html')
def team(request):
    return render(request,'team.html')

def resources(request):
    return render(request,'resources.html')

def appointment(request):
    if request.method == 'POST':
        myappointment=appointment(
            name =request.POST['full_name'],
            email = request.POST['email'],
            phone = request.POST['phone_number'],
            date = request.POST['date'],
            message = request.POST['message']
        )

        myappointment.save()
        return redirect('/services')
    else:
        return render(request,'appointment.html')


def show(request):
    allcontacts=Contact.objects.all()
    return render(request,'show.html',{'contact':allcontacts})






