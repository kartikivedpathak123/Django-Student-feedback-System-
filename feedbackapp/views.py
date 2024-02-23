from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import FeedbackForm
from feedbackapp.models import Feedback

# Create your views here.
def home(request):
    a= Feedback.objects.all()
    context={}
    context['data']=a
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def feedback(request):
    context={}
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        context['form']=form
        if form.is_valid():
            form.save()
            return redirect('/feedback_success')
    else:
        form = FeedbackForm()
        context['form']=form
    return render(request,'feedback.html',context)

def feedback_success(request):
    return render(request,'feedback_success.html')

def course(request):
    return render(request, 'course.html')

def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        context={}

        n=request.POST['uname']
        em=request.POST['email']
        p=request.POST['upass']
        cp=request.POST['ucpass']

        if n=='' or em=='' or p=='' or cp=='':
            context['errmsg']='Field can not be blank'
            return render(request,'signup.html',context)
        elif len(p)<=8:
            context['errmsg']='password must be atleast 8 character'
            return render(request,'signup.html',context)
        elif p!=cp:
            context['errmsg']='password and confirm password must be same'
            return render(request,'signup.html',context)
        else:
            try:
                u=User.objects.create(username=n,email=em)
                u.set_password(p )
                u.save()
                context['success']='User Created Successfully'
                return render(request,'signup.html',context)
            except Exception:
                context['errmsg']="User already Exist, Please Login!"
                return render(request,'signup.html',context)
            
def signin(request):
    if request.method=='GET':
        return render(request,'signin.html')
    else:
        n=request.POST['uname']
        p=request.POST['upass']
        
        u=authenticate(username=n,password=p)
        if u is not None:
            login(request,u)
            return redirect('/home')
        else:
            context={}
            context['errmsg']='Invalid Username and Password'
            return render(request,'signin.html',context)
        
def signout(request):
    logout(request)
    return redirect('/home')

        