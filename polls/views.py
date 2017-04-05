from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from polls.models import todo


# Create your views here.
def index(request):
    ret={}
    ret['name']=request.GET.get('id')
    #ret['length']=range(len(ret['name']))
   
    print(ret)
    print(request)
    return render(request,'login.html',ret)
def list_todo(request):
    ret={}
    if request.method=="POST":
        t = todo(text=request.POST.get('todo'))
        t.save()
        print()
    ret['todo']=todo.objects.all()
    return render(request,'todo.html',ret)
def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password= request.POST.get('password')
        print(username,password)


    return render(request,'login.html')
def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password= request.POST.get('password')
        password2=request.POST.get('password2')
        if(password==password2):
            user=User.objects.create_user(username=username,password=password)
            return redirect('/loginpage')
        else:
            return render(request,'signup.html',{'msg':"passwords does not match"})





    return render(request,'signup.html')

def todo_delete(request):
    pass
    # ret={}
    # ret
    # todo.objects.get(pk=).delete()

    


    
