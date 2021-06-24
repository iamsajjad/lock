from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Users, UsersLogin

# Create your views here.

@login_required(login_url='/')
def homepage(request):
    userinfo = Users.objects.get(id=request.user.id)
    response = {
        'user' : userinfo
    }
    return render(request, "homepage.html", response)

@login_required(login_url='/')
def changePattern(request):
    userinfo = Users.objects.get(id=request.user.id)
    response = {
        'user' : userinfo
    }
    return render(request, "author/changePattern.html", response)

@login_required(login_url='/')
def saveChanges(request):

    fname = request.POST.get('fname', '')
    lname = request.POST.get('lname', '')
    email = request.POST.get('email', '')
    pattern = request.POST.get('pattern', '')

    userinfo = User.objects.get(id=request.user.id)
    userinfo.email=email
    userinfo.set_password(pattern)

    user_account = Users.objects.get(username=str(request.user))
    user_account.fname=fname
    user_account.lname=lname
    user_account.pattern=pattern
    user_account.email=email

    user_login = UsersLogin.objects.get(username=str(request.user))
    user_login.pattern=pattern

    userinfo.save()
    user_account.save()
    user_login.save()
    login(request, userinfo)

    return HttpResponseRedirect('/home/')

def loginPage(request):
    return render(request, 'author/login.html')

def accountsPage(request):

    return render(request, 'author/author.html')

def signIn(request):

    username = request.POST.get('username', '')
    pattern = request.POST.get('pattern', '')
    user = authenticate(request, username=username, password=pattern)
    author = str(username)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect('/')

def signUp(request):

    username = request.POST.get('username', '')
    fname = request.POST.get('fname', '')
    lname = request.POST.get('lname', '')
    email = request.POST.get('email', '')
    pattern = request.POST.get('pattern', '')

    try:
        user = User.objects.create_user(username=username, email=email, password=pattern)

        Users.objects.create(username=username, fname=fname, lname=lname,
                             pattern=pattern, email=email).save()
        UsersLogin.objects.create(username=username, pattern=pattern).save()

        user.is_staff = True
        user.is_superuser = True
        user.save()
    except:
        return HttpResponseRedirect('/')
    else:
        author = str(username)
        return signIn(request)


def signOut(request):

    logout(request)

    return render(request, 'author/author.html')
