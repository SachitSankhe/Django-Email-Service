from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.
def send(request):

    msg_plain = render_to_string('email.txt')
    msg_html = render_to_string('email.html')

    send_mail("Email Service is working Properly",
    msg_plain,
    settings.EMAIL_HOST_USER,
    [settings.RECIEVER_EMAIL],
    html_message=msg_html)

    return render(request,'index.html')