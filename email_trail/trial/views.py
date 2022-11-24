from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.http import HttpRequest
from django.urls import reverse
# Create your views here.
def send(request):
    if request.method=="POST":
        # HttpRequest.get_full_path()
        print(HttpRequest.get_host(request))
        email = request.POST.get("email")

        context = {
            'link' : "https://" + str(HttpRequest.get_host(request)) + "/email/",
        }
        msg_plain = render_to_string('email.txt')
        msg_html = render_to_string('email.html',{'context':context})
        


        send_mail("Email Service is working Properly",
        msg_plain,
        settings.EMAIL_HOST_USER,
        [email],
        html_message=msg_html)

        messages.success(request,"Email has been sent successfully")
        
        return render(request,'index.html')
        
    else:
        return render(request,'index.html')
