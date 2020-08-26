from django.urls import path
from . import views


app_name='emails'



urlpatterns = [

    path('send-emails',views.send_email, name='home'),

]