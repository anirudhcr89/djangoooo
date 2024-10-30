from django.shortcuts import render,redirect
from .models import usermodel,mediause
from .forms import userform
from django.http import HttpResponse
# Create your views here.
def get_all(request):
    data=usermodel.objects.all()
    return render(request,'get_all.html',{'data1':data})
def add_user(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        date=request.POST.get('date')
        age=request.POST.get('age')
        user_obj=usermodel()
        user_obj.username=name
        user_obj.user_date=date
        user_obj.user_age=age
        user_obj.save()
        return redirect('get')
    return render(request,"add_user.html")
def delete_user(request,pk):
    user=usermodel.objects.get(id=pk)
    user.delete()
    return redirect('get')
def update(request,pk):
    user=usermodel.objects.get(id=pk)
    if request.method == 'POST':
        name=request.POST.get('name')
        date=request.POST.get('date')
        age=request.POST.get('age')
        user.username=name
        user.user_date=date
        user.user_age=age
        user.save()
        return redirect('get')
    return render(request,"update.html",{'user':user})
from django.shortcuts import render, redirect
from .forms import userform  # Ensure your import is correct

def loadfm(request):
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = userform()  
    return render(request, "user_load.html", {'form': form})
def log(request):
    return render(request,'login.html')
def Med(request):
    data=mediause.objects.all()
    return render(request,'media.html',{'data':data})
def loadme(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        place=request.POST.get('place')
        Image=request.FILES.get('Img')
        user_obj=mediause()
        user_obj.name=name
        user_obj.place=place
        user_obj.image=Image
        user_obj.save()
        return redirect('me')
    return render(request, "addmedia.html",)
def base(request):
    return render(request,'base.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render (request,'about.html')
def contact(request):
    return render(request,'contact.html')
  ##bulit in user and abstrat
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
# user = User.objects.create_user(username='john_doe', password='password123')
# user.save()
# def setpassword(request):
#     user = User.objects.get(username='anirudh1')  #/////
#     user.set_password('1234')
#     user.save()
# def checkpassword(request):      
#     user=User.objects.get(username='ani')
#     if user.check_password('12345'):                                      ##....path is not created
#         return HttpResponse(f'User authenticated successfully! username:{user.username}')
#     else:
 #         return HttpResponse('Password is incorect')    
# def log(request):
#     username=User.objects.get(username='anirudh1')

    # print(username.last_login)
    # return HttpResponse("done")  ## lasr login time

    # username.is_staff=True
    # username.save()     ##status will true 

    # username.is_superuser=True
    # username.save()

    # return HttpResponse('Done')
    # username='anirudh1'
    # password1='1234'
    # user=authenticate(username=username,password=password1)
    # if user is not None:
    #     return HttpResponse("successfully login")
    # else:
    #     return HttpResponse("user not vaild") 
  