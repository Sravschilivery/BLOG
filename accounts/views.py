from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth.models import User
from accounts.models import Profile
import os

from django.contrib.auth import authenticate ,login, logout

# Create your views here.

def user_login(request):

    if request.method=='GET':
        return render(request,'account/login.html')

    else:
        context={}
        uname=request.POST['uname']
        upass=request.POST['upass']

        if uname=='' or upass=='':
            context['errmsg']="Fields cannot be empty"
            return render(request,'account/login.html',context)
        
        else:
            u=authenticate(username=uname,password=upass)
            # print(u)
            if u is not None:
                login(request,u)
                return redirect('/')

            else:
                context['errmsg']="Invalid Username and Password"
                return render(request,'account/login.html',context)



def user_regisetr(request):

    if request.method=='GET':
        
        return render(request,'account/register.html')
    
    else:
        context={}
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']

        if uname=='' or uemail=='' or upass=='' or ucpass=='':
            context['errmsg']="Fields cannot be empty"
            return render(request,'account/register.html',context)

        elif upass!=ucpass:
            context['errmsg']="Password and Confirm Password Mismatched"
            return render(request,'account/register.html',context)
        
        elif len(upass)<8:
            context['errmsg']="Password should be 8 character"
            return render(request,'account/register.html',context)

        elif upass.isdigit():
            context['errmsg']="Password should not be entirly in digit"
            return render(request,'account/register.html',context)
    
        else:
            u=User.objects.create(username=uname,email=uemail)
            u.set_password(upass)
            u.save()

            context['success']="Registered Successfully"
            return render(request,'account/register.html',context)


def user_logout(request):
    logout(request)
    return redirect('/')


# Profile Management

def profile(request):
    context={}
    if request.method=='GET':
       
        try:
            p=Profile.objects.get(uid=request.user.id)
            context['pdata']=p
            return render(request,'account/profile.html',context)
        except:
            
            context['errmsg']="Please Update Your Profile...."
            return render(request,'account/profile.html',context)


    else:

        fname=request.POST['fname']
        lname=request.POST['lname']
        uemail=request.POST['email']
        mob=request.POST['mob']
        uadd=request.POST['uadd']
        try:
            uimg=request.FILES['uimg']
        except:
            context['errmsg']="Fields cannot be empty..."
            return render(request,'account/profile.html',context)

        if fname=='' or lname=='' or uemail=='' or mob=='' or uadd=='':
            context['errmsg']="Fields cannot be empty..."
            return render(request,'account/profile.html',context)
        
        else:
            p=Profile.objects.filter(uid=request.user.id)
            if len(p)==0:
                u=User.objects.filter(id=request.user.id)
                u.update(first_name=fname,last_name=lname,email=uemail)

                u_obj=User.objects.get(id=request.user.id)
                up=Profile.objects.create(mob_no=mob,uimg=uimg,uadd=uadd,uid=u_obj)
                up.save()
                return redirect('/account/profile')
            else:

                u=User.objects.filter(id=request.user.id)
                u.update(first_name=fname,last_name=lname,email=uemail)

                up=Profile.objects.get(uid=request.user.id)

                up.mob_no=request.POST['mob']
                up.uadd=request.POST['uadd']
                if len(request.FILES) != 0:
                    if len(up.uimg) > 0:
                        os.remove(up.uimg.path)
                    up.uimg=request.FILES['uimg']
                up.save()
                return redirect('/account/profile')
                    
                
                
                    

        