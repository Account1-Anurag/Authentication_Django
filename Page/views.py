from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Home (Login) Page
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful!")
            return redirect("/")  # Stay on the home page (or change as needed)
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "index.html", {"messages": messages.get_messages(request)})  # Pass messages properly

# Signup View
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
        else:
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("index")  # Redirect to login page

    return render(request, "signup.html", {"messages": messages.get_messages(request)})  # Pass messages properly


