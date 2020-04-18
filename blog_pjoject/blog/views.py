from django.shortcuts import render, redirect
from .forms import ContactUsForm, SignUpForm, LoginForm
from django.core.mail import EmailMessage
from django.conf import settings
from .models import Post, Author
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    if request.method == 'POST':
        form1 = SignUpForm(request.POST)
        form2 = LoginForm(request.POST)
        if form2.is_valid():
            uname = request.POST.get('name')
            passd = request.POST.get('pswd')
            user = authenticate(request, username=uname, password=passd)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome {user.username.upper()}! You are logged in.")
                return redirect('blog:home')
        else:
            messages.error(request, 'Please Correct the errors!')

        if form1.is_valid():
            form1.save()
            name = request.POST.get('username')
            messages.success(request, f'{name} account created successfully')
            return redirect('blog:home')
        else:
            messages.error(request, 'Please Correct the errors!')
    else:
        form1 = SignUpForm()
        form2 = LoginForm()
    context = {
                'form1' : form1,
                'form2' : form2,
               }
    return render(request, 'blog/index.html', context)

def logout_view(request):
	logout(request)
	messages.success(request, f"Thanks for using our web services.You are logged out")
	return redirect('blog:home')


def posts_view(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog/posts.html', context)

class PostsList(ListView):
    model = Post
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post

class AuthorsList(ListView):
    model = Author
    paginate_by = 12

class AuthorDetailView(DetailView):
    model = Author

def user_view(request):
    context = {}
    return render(request, 'blog/user.html', context)

def post_view(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post': post}
    return render(request, 'blog/post.html', context)

def contact_mail(request):
    if request.method=="POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            print("DATA IS VALIDATED")

            name = request.POST.get('name')
            mail = request.POST.get('email')
            sub = request.POST.get('subject')
            meassage = request.POST.get('body')

            email = EmailMessage(
                'Hello! You got a mail from '+"mail",
                "Name : "+str(name)+'\n'
                f"Email : {str(mail)} \n"
                f"Subject : {str(sub)} \n"
                f"Meassage : {str(meassage)} \n",
               settings.EMAIL_HOST_USER, # 'from@example.com',
                ['nagaraj015973@gmail.com', 'love.haters.fully@gmail.com'], # to@example.com',
            )
            email.send(fail_silently=False)
            form.save()
            print("DATA SAVED TO THE DATABASE")
            return redirect('blog:home')
    else:
        form = ContactUsForm()
    context = {
        "form" : form,
    }
    return render(request, 'blog/contactus.html', context)