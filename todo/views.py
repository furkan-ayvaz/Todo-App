from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import TODO
from django.contrib import messages
from .forms import todo_form
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="user:login")
def dashboard(request):
    todos = TODO.objects.filter(inserted_by=request.user)
    return render(request,"dashboard.html",{"todos":todos})
   

@login_required(login_url="user:login")
def todoAdd(request):
    form = todo_form(request.POST or None)
    if form.is_valid():
        todo_describe = form.cleaned_data.get("todo_describe")
        newTodo = TODO(todo_describe=todo_describe)
        newTodo.inserted_by = request.user
        newTodo.save()
        messages.success(request,"Todo added successfully ...")
        return redirect("todo:dashboard")
    return render(request,"todoAdd.html",{"form":form})

@login_required(login_url="user:login")
def todoUpdate(request,id):
    todo = get_object_or_404(TODO,id = id)
    todo_describe = todo.todo_describe
    todo_case = todo.todo_case
    todo.delete()
    if todo_case == True:
        todo_case = False
    else:
        todo_case = True
    newTodo = TODO(id = id,todo_describe = todo_describe,todo_case=todo_case)
    newTodo.inserted_by = request.user
    newTodo.save()
    messages.success(request,"Todo update successfully ...")
    return redirect("todo:dashboard")

@login_required(login_url="user:login")
def todoDelete(request,id):
    todo = get_object_or_404(TODO,id = id)
    todo.delete()
    messages.success(request,"Todo deleted successfully ...")
    return redirect("todo:dashboard")


    