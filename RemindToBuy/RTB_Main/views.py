from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from allauth.account.decorators import login_required 
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

import pyrebase

# Create your views here.
config = {
    "apiKey": "AIzaSyBreRHSGACvbjag89Czr17tCIp0rRm5YZc",
    "authDomain": "remindtobuy-v1.firebaseapp.com",
    "databaseURL": "https://remindtobuy-v1.firebaseio.com",
    "storageBucket": "remindtobuy-v1.appspot.com",
    "projectId": "remindtobuy-v1",
    "messagingSenderId": "778812133495",
    "appId": "1:778812133495:web:b7daf404137dfca5ccb672",
    "measurementId": "G-8CJ2MWM5ZM"
}
firebase = pyrebase.initialize_app(config)
@login_required
def index(request):
    return render(request, "index.html")

@login_required
def profile(request):
    return render(request, "profile.html")

@login_required
def product(request):
    return render(request, "product.html")

@login_required
def add_product(request):
    return render(request, "add_product.html")

@login_required
@require_http_methods(["POST"])
def save_product(request):
    user_email = SocialAccount.objects.filter(user=request.user)[0].extra_data["email"]
    product_url = request.POST["input_product_url"]
    site = request.POST["input_site"]
    price = request.POST["input_price"]
    email_address = request.POST["input_email_address"]
    
    db = firebase.database()
    db.child("products")
    data = {
        "user_email" : user_email,
        "product_url": product_url,
        "site": site,
        "price": price,
        "email_address": email_address
    }
    print(data)
    db.child("products").push(data)
    return render(request, "add_product.html")



def login(request):
    #print user
    user = request.user
    if str(user) is not "AnonymousUser":
        #social_info = SocialAccount.objects.filter(user=request.user)[0].extra_data
        #print(social_info)
        return redirect("/")
    else:
        return render(request, "login.html")            
    
