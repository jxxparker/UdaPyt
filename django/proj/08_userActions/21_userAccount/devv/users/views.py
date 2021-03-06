from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm


def loginUser(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("profiles")


    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profiles")
        else:
            messages.error(request, "Username OR password is incorrect")

    return render(request, "users/loginRegis.html")


def logoutUser(request):
    logout(request)
    messages.info(request, "Username was logged out")
    return redirect("loginUser")

def registerUser(request):
    page = "register"
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created!")
            login(request, user)
            return redirect("profiles")

        else:
            messages.error(request, "An error has occurred during registration")
            

    context = {"page": page, "form": form}
    return render(request, "users/loginRegis.html", context)



def profiles(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, "users/profiles.html", context)


def userProfile(request, pk):
    userProfile = Profile.objects.get(id=pk)
    topSkills = userProfile.skill_set.exclude(description__exact="")
    otherSkills = userProfile.skill_set.filter(description="")

    context = {
        "userProfile": userProfile, 
        "topSkills": topSkills, 
        "otherSkills": otherSkills
    }
    return render(request, "users/userProfile.html", context)
    

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile

    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    
    context = {
        "profile": profile,
        "skills": skills,
        "projects": projects
         }
    return render(request, "users/account.html", context)