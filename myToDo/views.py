from django.shortcuts import render,redirect
from django.http import HttpResponse
from myToDo.models import ToDo
from myToDo.forms import ToDoForm

def home(request):
    todo_list = ToDo.objects.all() # ORM model - This is how we fetch data from the backend ie (modelname.objects.operation)
                                   # In return we get the queryset
    template_name = 'home.html'
    #print(todo_list)             # just to check what it queryset we get in return.... we can check this in terminal after running our server
    form = ToDoForm()      # creating todo form object instance
    context = {'app_name' : "ToDo App",'todo_list': todo_list , 'form': form}
    return render(request, template_name,context = context)

def add_todo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            text_t= form.cleaned_data.get('text_todo')  #if the form is validated then the querydic will be stored in text_t
            ToDo.objects.create(text_todo = text_t)    # creates new field in data to save text_t thru form model text_todo field


    return redirect('Home')  

def delete_todo(request,todo_id):
    if request.method == 'POST':
        obj =  ToDo.objects.get(pk = todo_id)  # passing the object value(pk : primary key) to access it
        obj.delete()
    return redirect('Home')

def edit_todo(request,todo_id):
    
    template_name = 'edit.html'
    obj = ToDo.objects.get(pk = todo_id)
    form = ToDoForm(initial={'text_todo': obj.text_todo})
    context = {'app_name' : "ToDo App",'form': form, 'obj': obj}
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            obj.text_todo = form.cleaned_data.get('text_todo')
            obj.save()
            return redirect('Home')


    return render(request,template_name, context = context)
   
#background: #719e77 ;
           

