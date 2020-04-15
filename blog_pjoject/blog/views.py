from django.shortcuts import render, redirect
from .forms import ContactUsForm
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'blog/index.html')

def haha(request):
    return render(request, 'blog/base.html')

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