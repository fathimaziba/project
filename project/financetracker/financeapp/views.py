# Import necessary modules
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm  # Correct form import
from django.contrib.auth.decorators import login_required  # Correct spelling of decorators

# Home and other basic views
def index(request):
    return render(request, 'index.html')

"""def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            return render(request, 'user_login.html', {'error': 'Invalid credentials'})

    return render(request, 'user_login.html')  # Render login page if not POST"""
def login(request):
    return render(request,'login.html')

def sign_up_view(request):
    return render(request, 'sign-up.html')

def support_view(request):
    return render(request, 'support.html')
def admin(request):
    pass

def user_view(request):
    return render(request, 'user.html')


# Register new user using Django's UserCreationForm
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Correct usage of UserCreationForm
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()  # Display empty form initially

    return render(request, 'userregister.html', {'form': form})  # Render registration page

def dashboard(request):
    return render(request,'dashboards.html')

def transaction(request):
    return render(request,'transaction.html')
def accounts(request):
    return render(request,'accounts.html')
def income_expense(request):
    return render(request,'income&expense.html')
def profile(request):
    return render(request,'profile.html')
def new_transaction(request):
    return render(request,'new_transaction.html')
def income(request):
    return render(request,'income.html')
def expense(request):
    return render(request,'expense.html')