from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json
import googlemaps
from django.conf import settings
from datetime import datetime
from rest_framework.response import Response
 
from .models import Feedback, Profile
from .serializers import Feedbackserializer
import requests
# from .forms import ProfileForm

from .models import Temple

#  @login_required(login_url="/register")
def homepage(request):
    temples = Temple.objects.all()
    return render(request,"temple.html", {'temples':temples})


@login_required(login_url="register/")
def temple_info(request):
    name = request.GET.get("name") 
    print(name)
    temple = Temple.objects.filter(name=name).first()
    print(temple)
    return render(request, "info.html", {'temple':temple})

@login_required(login_url="register/")
def search_info(request):
    city = request.GET.get('city')
    print(city)
    if city != None:
        temples = Temple.objects.filter(city__icontains=city)
        return render(request, "searchinfo.html", {'temples': temples})
    
    state = request.GET.get('state')
    print(state)
    if state != None:
        temples = Temple.objects.filter(state__icontains=state)
        return render(request, "searchinfo.html", {'temples':temples})

    name = request.GET.get('name')
    print(name)
    if name != None:
        temples = Temple.objects.filter(name__icontains=name)
        print(temples)
        return render(request, "searchinfo.html", {'temples':temples})

    return render(request,"searchinfo.html")

def searchpage(request):
    # temples = Temple.objects.all()
    # cities = Temple.objects.filter(name__icontains=name)
    # states = Temple.objects.filter(name__icontains=name)
    # temples_list = []
    # for temple in temples:
    #     temples_list.append(temple.city)
 
    # temples_list = json.dumps(temples_list) 
    # print(temples_list)
    
    return render(request,"search.html")

def aboutpage(request):
    return render(request,"about.html")

def registerationpage(request):
    if request.method == "POST":
        isLogin = request.POST.get('login')
        print(isLogin)
        if isLogin == 'True':
            print("login")
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                messages.error(request, "Invalid Credentials")
                return redirect("/register")
        else:
            print("registration")
            username=request.POST.get('username')
            password=request.POST.get('password')
            confirm_password=request.POST.get('confirm-password')
            if User.objects.filter(username=username).exists():
                messages.error(request,"User is already exists!")
            else:
                if password == confirm_password:
                    user=User.objects.create_user(username=username,password=password)
                    user.save()
                    profile=Profile.objects.create(user=user)
                    profile.save()
                    messages.success(request,"User sign up successfully!")
                    print(str(user))
                else:
                    messages.error(request,"Incorrect Password")

        
    return render(request,"registration.html")

def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        
    return redirect("/register")


def profile(request):
    user_model = User.objects.get(username=request.user.username)
    profile_model = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        bio = request.POST['bio']
        profile_model.bio = bio
        profile_model.firstname = firstname
        profile_model.lastname = lastname
        
        #Handle image upload
        if 'photo' in request.FILES:
            profile_model.photo = request.FILES['photo']
        profile_model.save()
        user_model.save()
        messages.success(request,'Updated successfully')
    return render(request,"profile.html",{'user_model':user_model, 'profile_model': profile_model})


def learnpage(request):
    if request.method =='POST':
        print(request.POST)
        content=request.POST['feedback']
        print("content : ",content)
        feedback = Feedback.objects.create(content=content,user=request.user, content_at=datetime.now())
        print(feedback)
        feedback.save()
    return render(request,"learn.html")
def nearbypage(request):
    temples = Temple.objects.all()
    temple_data = [{'name': temple.name, 'latitude': temple.latitude, 'longitude': temple.longitude} for temple in temples]
    temple_data_json = json.dumps(temple_data)
    return render(request, "nearbyme.html", {'temple_data_json': temple_data_json})

def calculate_route(request):
    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')

        # Initialize Google Maps client with your API key
        gmaps = googlemaps.Client(key=settings.AIzaSyByw2ycN8WG448Ef_H4Pa4C62appI6fRtI)

        # Get directions
        directions = gmaps.directions(origin, destination)

        # Extract relevant information from directions
        steps = []
        for step in directions[0]['legs'][0]['steps']:
            steps.append(step['html_instructions'])

        # Return the response
        return JsonResponse({'steps': steps})

    # Handle if method is not POST
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required(login_url="register/")
def submit_feedback(request):
    if request.method =='POST':
        content=request.POST['feedback']
        print("content : ",content)
        feedback = Feedback.objects.create(content=feedback,user=request.user, content_at=datetime.now())
        print(feedback)
        feedback.save()


@login_required(login_url="register/")
def delete_feedback(request, feedback_id):
    feedback = Feedback.objects.get(pk=feedback_id)
    feedback.delete()
    return JsonResponse({'error','Feedback deleted successfully'}, status=200)


def index(Request):
    return render(Request,'index.html')