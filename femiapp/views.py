from django.http import HttpResponse
from django.shortcuts import render, redirect
from femiapp.forms import postForm
from femiapp.models import Contact, Post, User, Admin
from femiapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from requests.auth import HTTPBasicAuth
import requests
import json


# Create your views here.

def delete(request,id):
    message =Contact.objects.get(id=id)
    message.delete()
    return redirect('/show')
def index(request):
    if request.method == 'POST':
        if User.objects.filter(
            username=request.POST['username'],
            password=request.POST['password']
        ).exists():
            return render(request,'index.html')
        else:
            return render(request,'login.html')

    else:
        return render(request,'login.html')

def service(request):
    return render(request,'service.html')

def femicide(request):
    return render(request,'femicide.html')

def about(request):
    return  render(request,'about.html')

def contact(request):
    if request.method == "POST":
        mycontact=Contact(
            fullname = request.POST['name'],
            phone= request.POST['phone'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],

        )
        mycontact.save()
        return redirect('/contact')
    else:
        return render(request,'contact.html')

def post(request):
   if request.method == "POST":
       form = postForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('/story')
   else:
        form = postForm()
   return render(request,'post.html',{'form':form})


def story(request):
    story = Post.objects.all()
    return  render(request,'story.html',{'story':story})

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        members=User(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password'],
        )
        members.save()
        return redirect('/login')
    else:
        return render(request,'register.html')



def token(request):
    consumer_key = 'jKOHoU9BPhN4irqozAY4NCIAW5Y4b6tVvYjXRx0pGsyTZJNv'
    consumer_secret = '6mQvRzDoNtqeTkfQLC24A6rg1jWwAjtnb9ypNXvnabWjcHuD1CzNTlwA4oZu2nVz'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "eMobilis",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("confirm your Mpesa PIN to complete Donation")

def login2(request):
    return render(request,'login2.html')

def show(request):
    messages = Contact.objects.all()
    if request.method == "POST":
        if Admin.objects.filter(
                username=request.POST['username'],
                password=request.POST['password']
        ).exists():
            return render(request, 'show.html', {'message': messages})
        else:
            return render(request,'login2.html')
    else:
        return render(request, 'login2.html')

