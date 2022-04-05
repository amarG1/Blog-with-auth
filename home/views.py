from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login/")
    return render(request, 'home.html')

def loginuser(request):
    if request.method=="POST":
       username = request.POST['username']
       password = request.POST['password']
    #    username = User.objects.get(email=email.lower()).username
       user = authenticate(request, username=username, password=password)
    
       if user is not None:
            # template = render_to_string('email_template.html',{'name':request.user.profile.first_name} )
            # email = EmailMessage(
            #         'thank you! ',
            #         template,
            #         settings.EMAIL_HOST_USER,
            #         [request.user.profile.email],
            #                )
            # email.fail_silently=False
            # email.send()
            login(request, user)
            return redirect("/")
            # Redirect to a success page.
            
        
       else:
          # Return an 'invalid login' error message.
          return render(request, 'login.html')
    return render(request, 'login.html')

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def reg(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already taken')
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'email taken')
                return redirect('/register/')

                # print('email taken')    
            else :
                user =User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.success(request, 'Successfully registered you can login now.')
                return redirect('/')

                # email = EmailMessage(
                #     'Subject here',
                #     'body',
                #     settings.EMAIL_HOST_USER,
                #     ['to@example.com'],
                #      )
                # email.fail_silently=False
                # email.send()
                
                # print('user_created') 

        else:
                messages.warning(request, 'password not matching.')
                return redirect('/register/')

            # print('password not matching.')                                                                                                                      
    else:
     return render(request,'register.html')


def logoutuser(request):
    logout(request)
    return redirect("/login/")