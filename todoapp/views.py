from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def createUser(data):
    user =User.objects.create_user(username=data['username'], password=data['password'],email=data['email'])
    return user
def Home(request):
    msg='you are logged in'
    isLogged= False
    clients =Client.objects.all()
    print(request.user)
    if request.user.is_authenticated:
        isLogged= True
        msg='welcome, '+request.user.username
    context={
        'clients':clients,
        'msg':msg,
        'isLogged':isLogged
        
    }
    return render(request,'home.html', context)


def createClient(request):
    
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        user_id= createUser({'username': name,'password':password, "email":email})
        Client.objects.create(user=user_id,phone_number=phone)
        return redirect(Home)
    
    
def deleteClient(request,id):
    Client.objects.get(id=id).delete()
    return redirect(Home)
 
def updatePage(request,id):
 if request.method =='GET':
    client =Client.objects.get(id=id)
    
    context ={
        'client': client
    }
    return render(request,'update.html',context)
 if request.method =='POST':
        name=request.POST['name']
        phone=request.POST['number']
        email=request.POST['email']
        
        client=Client.objects.get(id=id)
        client.email=email
        client.name=name
        client.phone_number=phone
        client.save()
        return redirect(Home)



def loggedIn(request):
    return render(request,'loggedIn.html')

def loginView(request):
    if request.method=='GET':
        return render(request,'login.html')
        
    if request.method=='POST':
       Username=request.POST['username']
       password=request.POST['password']
       user = authenticate(username=Username, password=password)
       if user is not None:
         login(request,user)
         return redirect(Home)


def logoutView(request):
    logout(request)
    return redirect(Home)


