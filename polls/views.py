from django.shortcuts import render
from django.http import HttpResponse
from polls.models import todo


# Create your views here.
def index(request):
    ret={}
    ret['name']=request.GET.get('name')
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


    


    
