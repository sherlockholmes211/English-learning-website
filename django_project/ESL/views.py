from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import ExamQ,ExamV,TMarks,Dmarks,Profile
from .forms import ContactForm,SnippetForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,CustomUserCreationForm,UserForm,ExamQt,ExamVt
from django.contrib import auth
from datetime import datetime
from django.contrib import messages
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your views here.

def login(request):#login
    return render(request,'ESL/login.html')

def home(request):#home page or first page in app
    return render(request,'ESL/home.html')

def learning(request):#learning page in webapp
    return render(request,'ESL/learning.html')

def Contact_Us(request):#contact page in webapp
    return render(request,'ESL/Contact_Us.html')

def home2(request):#home page After Sign-in of User redirect
    return render(request,'ESL/home2.html')

def exam(request):#videos Page
    return render(request,'ESL/video.html')

def exam_genre(request):#videos/genre Page
    return render(request,'ESL/video_genre.html')

def exam_genre_exam(request):#videos/genre/exam Page
    return render(request,'ESL/video_genre_exam.html')

def audio(request):#audio Page
    return render(request,'ESL/audio.html')

def audio_genre(request):#audio/genre Page
    return render(request,'ESL/audio_genre.html')

def audio_genre_exam(request):#audio/genre/exam Page
    return render(request,'ESL/audio_genre_exam.html')

def about(request):#about page
    return render(request,'ESL/about.html')

def prac(request):#practice page
    profile = Profile.objects.get(user=request.user)
    TMark = TMarks.objects.get(UserI=request.user)
    Dmark = Dmarks.objects.filter(UserI=request.user).order_by('-id')[:7]
    return render(request, 'ESL/prac.html', {'TMarks': TMark, 'Dmarks': Dmark , 'Profile':profile})




def Ques(request):#Function Based View that Checks correct ans and saves it
    if request.method == 'POST':#if any thing enters
        form = ExamQt(request.POST)
        print("user")
        print(request.user.id)
        user = User.objects.get(username=request.user)#gets Active User instance
        print(user)
        if form.is_valid():
            n=0
            now = datetime.now()
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            qq=form.cleaned_data['q1']
            if qq == "dash": #if Ans is correct adds score
                n=1

            qq=form.cleaned_data['q2']
            if qq == "shock":
                n=n+1
            qq=form.cleaned_data['q3']
            if qq == "dash":
                n=n+1
            qq=form.cleaned_data['q4']
            if qq == "nail":
                n=n+1

            
            if TMarks.objects.filter(UserI=request.user).exists():
                TMark = TMarks.objects.get(UserI=request.user)
                TMark.tmarks = TMark.tmarks + n
                TMark.save()
            else:
                TMark = TMarks(UserI=request.user)
                TMark.tmarks = n
                TMark.save()

            if Dmarks.objects.filter(UserI=request.user,date_now=now.strftime("%Y-%m-%d")).exists():
                Dmark = Dmarks.objects.filter(UserI=request.user)[0]
                Dmark.dmarks = Dmark.dmarks + n
                Dmark.save()
            else:
                Dmark = Dmarks(UserI=request.user,date_now=now.strftime("%Y-%m-%d"))
                Dmark.dmarks = n
                Dmark.save()

            q=ExamQ(UserI=request.user)

            q.marks = n
            print("hi")
            #enters data into the q model
            q.User1=request.user
            q.q1=form.cleaned_data['q1']
            q.q2=form.cleaned_data['q2']
            q.q3=form.cleaned_data['q3']
            q.q4=form.cleaned_data['q4']
            q.save()
            form = ExamQt()
            print("success")
            query=q

            return render(request,'ESL/result.html',{'query':query})#Renders user marks html



    form = ExamQt()
    return render(request,'ESL/video_genre_exam.html',{'form':form})#Renders user Questions html

def QuesA(request):#Function Based View that Checks correct ans and saves it
    if request.method == 'POST':#if any thing enters
        form = ExamVt(request.POST)
        print("user")
        print(request.user.id)
        user = User.objects.get(username=request.user)#gets Active User instance
        print(user)
        if form.is_valid():
            n=0
            now = datetime.now()
            qq=form.cleaned_data['q1']
            if qq == "dash": #if Ans is correct adds score
                n=1

            qq=form.cleaned_data['q2']
            if qq == "shock":
                n=n+1
            qq=form.cleaned_data['q3']
            if qq == "dash":
                n=n+1
            qq=form.cleaned_data['q4']
            if qq == "nail":
                n=n+1

            if TMarks.objects.filter(UserI=request.user).exists():
                TMark = TMarks.objects.get(UserI=request.user)
                TMark.tmarks = TMark.tmarks + n
                TMark.save()
            else:
                TMark = TMarks(UserI=request.user)
                TMark.tmarks = n
                TMark.save()

            if Dmarks.objects.filter(UserI=request.user,date_now=now.strftime("%Y-%m-%d")).exists():
                Dmark = Dmarks.objects.filter(UserI=request.user)[0]
                Dmark.dmarks = Dmark.dmarks + n
                Dmark.save()
            else:
                Dmark = Dmarks(UserI=request.user,date_now=now.strftime("%Y-%m-%d"))
                Dmark.dmarks = n
                Dmark.save()
        
            q=ExamV(UserI=request.user)

            q.marks = n
            print("hi")
            #enters data into the q model
            q.User1=request.user
            q.q1=form.cleaned_data['q1']
            q.q2=form.cleaned_data['q2']
            q.q3=form.cleaned_data['q3']
            q.q4=form.cleaned_data['q4']
            q.save()
            form = ExamVt()
            print("success")
            query=q

            return render(request,'ESL/result.html',{'query':query})#Renders user marks html



    form = ExamVt()
    return render(request,'ESL/audio_genre_exam.html',{'form':form})#Renders user Questions html

def editprofile(request):#edit profile page
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid(): #
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('ESL-practice')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'ESL/editprofile.html', context)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

def loginpage(request):#login page
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        password =  request.POST['password']
        print(password)
        user = auth.authenticate(username=username, password=password)#checks users auth
        print(user)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return redirect('ESL-home2')
        else:
            return render(request, 'ESL/signin.html', {})
    return render(request, 'ESL/signin.html', {})


def profile(request):#profile page
    if request.user:
        query = request.user
        print('profile ki redirect ayinapudu')
        print(request.user)
        query = User.objects.filter(email=request.user.email)#filter current user instance

        return render(request, 'ESL/profile.html', {"query":query})
    else:
        return render(request, 'ESL/login.html', {})

        
def logot(request):#logot view
    auth.logout(request)#logout chestadhi
    return redirect("ESL-home")

def signup(request):#Function Based Signin View for first time user login
    if request.method == 'POST':
        form =  UserForm(request.POST)
        form.errors
        print(form.errors)

        if form.is_valid():
            user = User()
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])
            user.save()
            print(user)
            return redirect('ESL-home2')
    else:
        form =  UserForm()
    return render(request, 'ESL/signin.html', {'form': form})











def contact(request):#for practice nothing special
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email = form.cleaned_data['email']

            print(name)

    form = ContactForm()
    return render(request,'ESL/form.html',{'form':form})


def snippet_detail(request):#for practice nothing special
    if request.method == 'POST':
        form = SnippetForm(request.POST)

        if form.is_valid():
            form.save()
            name=form.cleaned_data['name']
            if name == "help":
                form = SnippetForm()
                return render(request,'ESL/form1.html',{'form':form})


    form = SnippetForm()
    return render(request,'ESL/form2.html',{'form':form})
