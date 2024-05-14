from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth.models import User
from userblogs.models import Userblog
from django.db.models import Q
import os
from django.core.mail import send_mail

# Create your views here.


# Display All Blogs
def blogs(request):
    context={}
    u=Userblog.objects.order_by('-id').all()
    context['alluser']=u

    return render(request,'blogs/index.html',context)

# Readmore blogs
def user_read_more(request,bid):
    context={}
    b=Userblog.objects.get(id=bid)
    context['bdata']=b
    return render(request,'blogs/user_readmore.html',context)


# Blogger Section
def user_blogs(request):
    context={}
    
    if request.user.is_authenticated:
        u=Userblog.objects.order_by("-id").filter(buid=request.user.id)
        context['ubdata']=u
        return render(request,'blogs/user_blogs.html',context)
    
    else:
        return redirect('/account/login')


# Add Blogs
def add_blog(request):
    context={}
    if request.user.is_authenticated:
        if request.method=='GET':
            return render(request,'blogs/user_blogs_add.html')
    
        else:
            bname=request.POST['bname']
            cat=request.POST['cat']
            title=request.POST['title']
            try:
                img=request.FILES['img']
            except:
                context['msg']="Fields cannot be empty"
                return render(request,'blogs/user_blogs_add.html',context)
            date=request.POST['date']
            sdesc=request.POST['sdesc']
            desc=request.POST['desc']

            if bname=='' or cat=='' or title=='' or img=='' or date=='' or sdesc=='' or desc=='':
                context['msg']="Fields cannot be empty"
                return render(request,'blogs/user_blogs_add.html',context)
            else:
                u_obj=User.objects.get(id=request.user.id)
                b=Userblog.objects.create(bname=bname,buid=u_obj,bcat=cat,btitle=title,bimages=img,bdate=date,bshort_description=sdesc,bdescription=desc)
                b.save()



                # Email Notification
                email_noti=User.objects.values_list('email',flat=True)
                # print(email_noti)
                eb=bname
                esubject="New Blog Uploaded by "+eb
                emsg=" Title: "+title+"\n Short-Decription: "+sdesc+"\n Read more...URL"

                send_mail(
                    esubject,                                      #  subject
                    emsg,                                           #  message
                    "parmanandsagar733@gmail.com",                    #  from@example.com
                    email_noti,                                        #    to@example.com
                    fail_silently=False,
                )
                return redirect('/user_blog')
                
            
# Update Blogs
def update_blog(request,bid):
    context={}
    if request.method=='GET':
        u=Userblog.objects.get(id=bid)
        context['bdata']=u
        return render(request,'blogs/user_blogs_update.html',context)
    
    else:
        bname=request.POST['bname']
        cat=request.POST['cat']
        title=request.POST['title']
        # img=request.FILES['img']
        # date=request.POST['date']
        sdesc=request.POST['sdesc']
        desc=request.POST['desc']
        
        if bname=='' or cat=='' or title=='' or sdesc=='' or desc=='':
            context['msg']="Fields cannot be empty"
            return render(request,'blogs/user_blogs_add.html',context)
        
        else:
            b=Userblog.objects.filter(id=bid)
            b.update(bname=bname,bcat=cat,btitle=title,bshort_description=sdesc,bdescription=desc)
            
            bb=Userblog.objects.get(id=bid)
            try:
                if len(request.FILES) != 0:
                    if len(bb.bimages) > 0:
                        os.remove(bb.bimages.path)
                bb.bimages=request.FILES['img']
            except:
                context['ubdata']=b
                context['msg']="Fields cannot be empty"
                return render(request,'blogs/user_blogs_add.html',context)
            bb.save()
            
            return redirect('/user_blog')

# Delete Blogs
def delete_blog(request,did):
    u=Userblog.objects.filter(id=did)
    u.delete()
    return redirect('/user_blog')

# Filter blogs
def blog_filter(request,bfilter):
    context={}
    q2=Q(bcat=bfilter)
    ub=Userblog.objects.filter(q2)

    context['alluser']=ub

    return render(request,'blogs/index.html',context)

# Search Blogs
def search(request):
    context={}
    x=request.GET['fin']

    q3=Q(bcat__icontains=x)
    q4=Q(btitle__icontains=x)

    ub=Userblog.objects.filter(q3 | q4)

    context['alluser']=ub

    return render(request,'blogs/index.html',context)

# Contact Us 
def contact(request):
    
    return render(request,'blogs/contact.html')