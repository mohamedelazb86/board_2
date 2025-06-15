from django.shortcuts import render,redirect
from .forms import SignupForm,ActivateForm
from django.core.mail import send_mail
from .models import Profile
from django.contrib.auth.models import User

def signup(request):
    '''
    - create new user
    - stop active this user
    - send email to this user
    - return redirect activate html
    '''
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            user=form.save(commit=False)
            user.is_active=False
            form.save()        # create new user and create ne profile
            # send email to this user
            profile=Profile.objects.get(user__username=username)
            send_mail(
            "Activate Code",
            f"Welcome mr  {username} \n pls use this code {profile.code} ",
            "r_mido99@yahoo.com",
            [email],
            fail_silently=False,
        )
            return redirect(f'/accounts/{username}/activate')

    else:
        form=SignupForm()

    
    return render(request,'accounts/signup.html',{'form':form})
def actiavte(request,username):
    '''
     - get code if thios code == profile code
     - profile.code  = ''
     - activate this user
     - return rediect login
    '''
    profile=Profile.objects.get(user__username=username)
    if request.method =='POST':
        form=ActivateForm(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code']
            if code == profile.code :
                profile.code =''

                user=User.objects.get(username=username)
                user.is_active=True
                # user.is_authenticated=True
                user.is_staff=True

                user.save()

                return redirect('/accounts/login')

    else:
        form=ActivateForm()
    return render(request,'accounts/activate_code.html',{'form':form})
