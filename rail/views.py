from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Train, Passenger,Ticket, Contact

# Create your views here.
def index(request):
    return render(request,'rail/index.html')

def pnrstatus(request):
    return render(request,'rail/pnrstatus.html')

def getpnrstatus(request):
    if request.method=="POST":
        pnr1 = request.POST.get('pnr')
        aadhar1 = request.POST.get('aadhar')
        
        if pnr1=="" or aadhar1=="":
            params = {"flag": True}
            return render(request,'rail/getpnrstatus.html',params)  
            
        tickets1 = Ticket.objects.filter(pnr_no=pnr1,aadhar_no=aadhar1)
        allTrains = []

        for item in tickets1:
            allTrains.append([item.name,item.gender,item.age,item.aadhar_no,item.train_name,item.date_of_journey, item.source, item.destination,item.reservation_status,item.seat_number,item.pnr_no,item.cost])
            
        params={"allTrains":allTrains,"flag":False}

        if len(allTrains)==0:
            params = {"flag": True}
        return render(request,'rail/getpnrstatus.html',params) 
    return render(request,'rail/getpnrstatus.html',{"flag": True})        

    

def remove(string):
    return string.replace(" ", "")

def searchtrain(request):
    return render(request,'rail/searchtrain.html')

def booktrain(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        aadhar_no = request.POST.get('aadhar', '')
        source = request.POST.get('sourcecity', '')
        destination = request.POST.get('destinationcity', '')
        train_name = request.POST.get('trainname', '')
        date_of_journey = request.POST.get('date', '')
        phone_no = request.POST.get('phone', '')
        passenger = Passenger(name=name, age=age, gender=gender, aadhar_no=aadhar_no, source=source,
                       destination=destination, train_name=train_name,date_of_journey=date_of_journey, phone_no=phone_no)
        passenger.save()
        id = passenger.id

        trains = Train.objects.all()
        value=0
        cost=0
        
        for item in trains:
            ch =item.train_name.lower()
            ch1=item.source.lower()
            ch2=item.destination.lower()

            if ch==train_name.lower() and ch1==source.lower() and ch2==destination.lower():
                value=item.seats_available
                cost = item.fare_in_rupees
                
        
        if value>0:
            ticket = Ticket(name=name,gender=gender,age=age,aadhar_no=aadhar_no,train_name=train_name,date_of_journey=date_of_journey, source=source, destination=destination,reservation_status="Confirm",seat_number=value,pnr_no = 5000+id,cost=cost)
            Train.objects.filter(train_name=train_name).update(seats_available=value-1)
            ticket.save()
        else:
            ticket = Ticket(name=name,gender=gender,age=age,aadhar_no=aadhar_no,train_name=train_name,date_of_journey=date_of_journey, source=source, destination=destination,reservation_status="Waiting List",seat_number=value,pnr_no = 5000+id,cost=cost)


        ticketstatus = True
        return render(request, 'rail/booktrain.html',{'ticketstatus': ticketstatus,'id': id})
    return render(request,'rail/booktrain.html')

def searchresult(request):
    source1 = request.GET.get('source')
    destination1 = request.GET.get('destination')

    allTrains = []
    trains = Train.objects.all()

    for item in trains:
        s1=item.source.lower()
        s2=item.destination.lower()

        if s1==source1.lower() and s2==destination1.lower():
            allTrains.append([item.train_name,s1,s2,item.seats_available,item.fare_in_rupees,item.depart_time,item.arrival_time])
    
    params={'allTrains':allTrains,"flag": False}

    if len(allTrains)==0:
        params = {"flag": True}
    return render(request,'rail/searchresult.html',params)

def pnrresult(request):
    return render(request,'rail/pnrresult.html')


def searchtrainresult(request):
    query = request.GET.get('name')
    trains = Train.objects.all()
    allTrains = []
    ticketstatus = True
    
    for item in trains:
        ch =item.train_name.lower()

        if ch==query.lower():
            allTrains.append([item.train_name,item.source,item.destination,item.seats_available,item.fare_in_rupees,item.depart_time,item.arrival_time])
            ticketstatus = False

    params = {"allTrains":allTrains,"ticketstatus":ticketstatus}

    if len(allTrains)==0:
        params = {"ticketstatus":True}

    return render(request,'rail/searchtrainresult.html',params)

def login(request):
    return render(request,'rail/login.html')

def signup(request):
    return render(request,'rail/signup.html')

def logout(request):
    return render(request,'rail/logout.html')

def contact(req):
    if req.method=="POST":
        name = req.POST.get('name','')
        email = req.POST.get('email','')
        subject = req.POST.get('subject','')
        text = req.POST.get('text','')
    
        cont = Contact(name=name, email=email,subject=subject,text=text)
        cont.save()
    return render(req,'rail/contact.html')

def about(req):
    return render(req,'rail/about.html')