from mainapp.models import Info
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , logout, authenticate
from django.contrib.auth.decorators import login_required
from mainapp.models import *

# Create your views here.
@login_required(login_url='/login')
def home(request):
    try:
        info = Info.objects.get(pk=request.user.id)
                
            
        context = {
                'info': info
                }
        
        return render(request,'home.html',context)
    except : 
        print("hello")
        
        return redirect('/info')

def reg(request):
    
    form = UserCreationForm()
    
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():            
            form.save()
            return redirect('/login')
    else:
        context = {
            'form' : form
        }
        return render(request,'regi.html',context)
    

def signin(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        user = authenticate(request, username=username , password=password)
        if user is not None:
            print(username)

            login(request,user)
            print(username)
            # ur = "/home/" +str(username)
            return redirect('/')
    else:
        return render(request,'login.html')


def logoutprosses(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def info(request):
    
    
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        
        email = request.POST.get('email')
        phone = request.POST.get('email')
        address = request.POST.get('email')
        Info(username=user,email=email,phone=phone,address=address).save()
        return redirect('/')    

    else:   
        return render(request,'info.html')


