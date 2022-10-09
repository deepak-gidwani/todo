from django.shortcuts import render, redirect
from .models import todo
# Create your views here.

def index(request):
    allobjects = todo.objects.all()
    if request.method == "POST":
        new_todo = todo(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/')

    return render(request,'index.html',{'todos' : allobjects})

def delete(request,pk):
    deleteTodo = todo.objects.get(id=pk)
    deleteTodo.delete()
    return redirect('/')
