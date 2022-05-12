 
from django.shortcuts import render,redirect
from .models import Todo
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .forms import TodoAddForm, TodoUpdateForm
from django.urls import reverse_lazy




# Create your views here.
def home(request):
    return render(request, 'todo_app/home.html')

class HomeView(TemplateView):
    template_name = 'todo_app/home.html'



def list_todos(request):
    todos=Todo.objects.all()  # burada (complated=false ) yazarsak buraya 
    context={
        'todos':todos
    }   
    
    return render(request, 'todo_app/todo_list.html',context)

class TodoListView(ListView):
    model= Todo
   # template_name = 'todo_app/todo_list.html'   # app/modelsname_list.html seklindeyazarsak bunu yazmaya gerek yok
    context_object_name='todos' # todo_list.html e object_list yazsaydik gerek yoktu buna 

def todo_create(request):


    form=TodoAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    context= {
        'form':form
    }
    return render(request, 'todo_app/todo_create.html', context)

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoAddForm
    # fields = ('title')
    template_name = 'todo_app/todo_create.html'  # app/modelname_form.html
    success_url = reverse_lazy('todo_list')

def todo_update(request,id):
    todo =Todo.objects.get(id=id)
    form = TodoUpdateForm(instance=todo)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    context = {
        'form':form,
    }
    return render(request, 'todo_app/todo_update.html', context)

class TodoUpdateView(UpdateView):
    model=Todo
    form_class = TodoUpdateForm
    template_name = 'todo_app/todo_update.html'
    success_url = reverse_lazy('todo_list')
   # pk_url_kwarg = 'id'







def todo_detail(request, id):        
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo 
    }
    return render(request, 'todo_app/todo_detail.html', context)

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == "POST":
        todo.delete()
        return redirect("todo_list")
    return render(request, "todo_app/todo_delete.html") 

class TodoDeleteView(DeleteView):
    model=Todo
    template_name = 'todo_app/todo_delete.html'
    success_url = reverse_lazy('todo_list')
    

