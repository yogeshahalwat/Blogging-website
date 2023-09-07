from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import SignUpForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

def sign_up(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=SignUpForm()
    context={
        "form":form
    }
    return render(request,"users/sign_up.html",context)

def login_view(request):
    if request.method=="POST":
        user=authenticate(username=request.POST["username"],password=request.POST["password"])
        if user is not None:
            login(request,user)
            return redirect("blog-index")
        else:
             return render(request, "users/login.html", {"error": "Invalid username or password.","form":AuthenticationForm()})
    else:
        return render(request,"users/login.html",{"form":AuthenticationForm()})

@login_required
def logout_view(request):
    if request.method=="POST":
        logout(request)
    return render(request,"users/logout.html")

@login_required
def profile(request):
    if request.method=="POST":
        user_form=UserUpdateForm(request.POST or None,instance=request.user)
        profile_form=ProfileUpdateForm(request.POST or None,request.FILES or None,instance=request.user.profilemodel) 
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")
    else:
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.profilemodel)
    context={
        "user_form":user_form,
        "profile_form":profile_form

    }
    return render(request,"users/profile.html",context)