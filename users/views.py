from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registerUser(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account created!')

            login(request, user)
            return redirect('profiles')

    context = {'page': page, 'form':form}
    return render(request, 'users/login_register.html', context)

def logoutUser(request):
    logout(request)
    messages.error(request,'User has successfully logged out!')
    return redirect('login')



def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile':profile, 'topSkills':topSkills, 'otherSkills':otherSkills}
    return render(request, 'users/user-profile.html', context)


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Username does not exist')
            return render(request, 'users/login_register.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # TO-DO:url params
            return redirect('profiles')
        else:
            messages.error(request,'Either USERNAME/PASSWORD is wrong')
    context = {}
    return render(request, 'users/login_register.html', context)