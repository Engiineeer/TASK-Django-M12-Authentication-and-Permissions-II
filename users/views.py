from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login , logout

from users.forms import UserSigninForm, UserSignupForm

# Create your views here.
def signup(req):
    form = UserSignupForm()
    if req.method == "POST":
        form = UserSignupForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect("movie-list")
    context = {"form": form}
    return render(req,"signup.html")

def signin(req):
    form = UserSigninForm()
    if req.method == "POST":
        form = UserSigninForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(req, auth_user)
                redirect("home")


    context = {"form": form}
    return render(req,"signin.html", context)

def signout(req):
    logout(req)
    return redirect("signin")