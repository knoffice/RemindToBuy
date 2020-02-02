from django.shortcuts import render
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
auth = firebase.auth()
def index(request):
    #user = auth.sign_in_anonymous()
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")
