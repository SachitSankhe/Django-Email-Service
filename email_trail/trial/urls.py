from django.urls import path
from .views import send

app_name = 'trial'

urlpatterns = [
    path(r"email/",send,name = 'send'),
    # path("reset/",index,name="index")
]