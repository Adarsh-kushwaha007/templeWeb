# from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.contrib import messages,auth



# def homepage(request):
#     return render(request,"temple.html")

# def searchpage(request):
#     return render(request,"search.html")
# def aboutpage(request):
#     return render(request,"about.html")
# def registerationpage(request):
#     if request.method == "POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         confirm_password=request.POST.get('confirm-password')
#         if User.objects.filter(username=username).exists():
#             messages.error(request,"User is already exists!")
#         else:
#             if password == confirm_password:
#                 user=User.objects.create_user(username=username,password=password)
#                 user.save()
#                 # profile=profile.objects.create(user=user ,user_type=type)
#                 # profile.save()
#                 messages.success(request,"User sign up successfully!")
#                 print(str(user))
#             else:
#                 messages.error(request,"Incorrect Password")
#     return render(request,"registration.html")
# def learnpage(request):
#     return render(request,"learn.html")
# def nearbypage(request):
#     return render(request,"near.html")


