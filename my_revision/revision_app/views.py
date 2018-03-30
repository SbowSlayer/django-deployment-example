from django.shortcuts import render
from revision_app.forms import RevisionUsersForm, RevisionUsersExtra

#

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request, 'revision_app/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def register(request):
    
    registered = False
    if request.method == "POST":
        user_form = RevisionUsersForm(data = request.POST)
        extra_form = RevisionUsersExtra(data = request.POST)
        
        
        if user_form.is_valid() and extra_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password) #this calls the widget that hashes the password and save it as a hashed password
            user.save()
            
            extra = extra_form.save(commit = False) #if we save it directly its gonna override our user built in stuff so we need to add it to user and not override it
            extra.user = user
            if 'profile_pic' in request.FILES:
                extra.profile_pic = request.FILES['profile_pic']
            extra.save()
            
            registered = True
        else:
            print(user_form.errors,extra_form.errors)
    else:
        user_form = RevisionUsersForm()
        extra_form = RevisionUsersExtra()
        
    return render(request,'revision_app/registration.html',{'user_form':user_form,
                                                            'extra_form':extra_form,
                                                            'registered':registered,
                                                           })


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username') #getting from html form input name
        password = request.POST.get('password')
        
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT FOUND ALKHANEZ")
        else:
            print("someone tryies to log in and failed")
            return HttpResponse("Invalid login ids")
    else:
        return render(request, 'revision_app/login.html',{})
    
    
    
    
    
    
    
    
    
    
    





