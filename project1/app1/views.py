from django.shortcuts import render
from .models import ToDo
from .forms import ToDoForm
from django.http import HttpResponseRedirect
# Create your views here.

def homepage(request):
    if request.method=="POST":
        fm= ToDoForm(request.POST)
        if fm.is_valid():
            tasks= fm.cleaned_data.get('tasks')
            completed=fm.cleaned_data.get('completed')
            created_at=fm.cleaned_data.get('created_at')
            reg= ToDo(tasks=tasks,completed=completed,created_at=created_at)
            reg.save()
        return HttpResponseRedirect("/home/")
    else:
        fm= ToDoForm()
        data=ToDo.objects.all()
        return render(request,'home.html',{'forms':fm,'datas':data})

def delete(request,id):
    data= ToDo.objects.get(pk=id)
    return render(request,'delete.html',{'ids':id})

def confirm_delete(request,id):
    data= ToDo.objects.get(pk=id)
    data.delete()
    return HttpResponseRedirect('/home/')

def update(request,id):
    if request.method=="POST":
        dt=ToDo.objects.get(pk=id)
        fm=ToDoForm(request.POST,instance=dt)
        if fm.is_valid():
            fm.save()
    else:
        dt=ToDo.objects.get(pk=id)
        fm= ToDoForm(instance=dt)
    return render(request, 'update.html', {'form':fm})








