from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import List
from .forms import AddTasks
from django.contrib.auth.decorators import login_required

# Create your views here.


# def home_page(request):
#     # infos = List.objects.filter(user=request.user)
#     infos = List.objects.all()
#     args = {'infos': infos}
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         author = authenticate(request, username=username, password=password)
#         if author is not None:
#             login(request,author)
#             messages.success(request,"You have been logged in !")
#             return redirect('home')
#         else:
#             messages.success(request,"Error logging in, please try again")
#             return redirect('home')
#     else:
#         return render(request, 'home.html', args)

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import List

def home_page(request):
    # Filter tasks by the logged-in user
    infos = List.objects.filter(user=request.user) if request.user.is_authenticated else []
    args = {'infos': infos}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        author = authenticate(request, username=username, password=password)
        
        if author is not None:
            login(request, author)
            messages.success(request, "You have been logged in!")
            return redirect('home')  # Redirect to the same home page or another view
        else:
            messages.error(request, "Error logging in, please try again")
            return redirect('home')

    return render(request, 'home.html', args)



@login_required(login_url='')
def logout_page(request):
    logout(request)
    messages.success(request, "You have been logged out !")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username = username, password =  password)
            login(request, user)
            messages.success(request, "Registration done successfully")
            return redirect('home')
    else:
        form = UserCreationForm()           
    return render(request, 'register.html', {'form':form})


@login_required(login_url='')
def user_task(request, pk):
    if request.user.is_authenticated:
        record = List.objects.get(id=pk)
        return render(request, 'info.html', {'record':record})
    else:
        messages.success(request,"Login or register to use more of the site...")
        return redirect('home')
    

@login_required(login_url='')
def delete_task(request, pk):
    if request.user.is_authenticated:
        del_it = List.objects.get(id=pk)
        del_it.delete()
        messages.success(request, "Task deleted succesfully")
        return redirect('home')
    else:
        messages.success(request,"Permission denied")
        return redirect('home')
    


@login_required(login_url='')
def add_task(request):
    form = AddTasks(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save(user=request.user)
                messages.success(request,"Task Added!")
                return redirect('home')
        return render(request, 'add_task.html', {'form':form})
    else:
        messages.success(request, "Permission Denied...")
        return redirect('home')
    


# @login_required(login_url='')
# def update_task(request, pk):
#     if request.user.is_authenticated:
#         item = List.objects.get(id=pk)
#         form = AddTasks(request.POST or None, instance = item)
#         if request.method == 'POST':
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "Task Updated...")
#                 return redirect('home')
#         return render(request, 'update.html', {'form': form})
#     else:
#         messages.success(request, "Permission denied")
#         return redirect('home')



@login_required(login_url='/login/')
def update_task(request, pk):
    # Retrieve the task or show 404 if not found
    item = get_object_or_404(List, id=pk)
    infos = List.objects.filter(user=request.user)
    
    # Create form instance with the existing task (for update)
    form = AddTasks(request.POST or None, instance=item)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Task Updated...")
            return redirect('home')  # Redirect after successfully updating
    
    # Render the form if it's a GET request or if form is not valid
    return render(request, 'update.html', {'form': form, 'item': item})
        
