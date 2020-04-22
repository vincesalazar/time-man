from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, Task, Collection

def index(request):
    return render(request, 'index.html')

def register(request):
    post = request.POST
    errors = User.objects.basic_validator(post)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    lowerCaseEmail = post['email'].lower()
    if User.objects.filter(email = lowerCaseEmail).exists():
        messages.error(request, "That email already exists")
        return redirect('/')
    capitalizedFirstName = post['first_name'].capitalize()
    capitalizedLastName = post['last_name'].capitalize()
    password = post['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(
        first_name = capitalizedFirstName, 
        last_name = capitalizedLastName, 
        email = lowerCaseEmail, 
        password = pw_hash
    )
    Collection.objects.create(
        title = "General",
        desc = "Things that just need to get done.",
        user = user
    )
    request.session['user_id'] = user.id
    return redirect('/homepage')

def login(request):
    post = request.POST
    lowerEmail = post['email'].lower()
    try:
        user = User.objects.get(email = lowerEmail)
    except:
        messages.error(request, "Please check your password or email.")
        return redirect('/')

    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session["user_id"] = user.id
        return redirect('/homepage')
    else:
        messages.error(request, "please check your email and password.")
        return redirect('/')

def homepage(request):
    if "user_id" not in request.session:
        messages.error(request, "Must be logged in")
        return redirect('/')
    user_id = request.session['user_id']
    context = {
        "user": User.objects.get(id=user_id),
        "user_tasks": Task.objects.filter(user_id = request.session['user_id']).order_by('-created_at')
    }
    return render(request, 'homepage.html', context)

def addTask (request):
    if "user_id" not in request.session:
        messages.error(request, "Must be logged in")
        return redirect('/')
    
    user_id = request.session['user_id']

    context = {
        "user": User.objects.get(id=user_id),
        "tasks": Task.objects.filter(user_id = request.session['user_id']).order_by('-created_at')
    }
    return render(request, "addTask.html", context)

def logout(request):
    request.session.clear()
    return redirect('/')

def createGenTask(request):
    if "user_id" not in request.session:
        messages.error(request, "Must be logged in")
        return redirect('/')
    post = request.POST
    errors = Task.objects.basic_validator(post)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/homepage')
    Task.objects.create(
        content = post['content'].capitalize(),
        user = User.objects.get(id = request.session['user_id']),
        collection = Collection.objects.get(title = "General")
    )
    return redirect('/homepage')





















