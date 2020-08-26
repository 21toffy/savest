from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, send_mass_mail
from django.contrib.auth.models import User
# from django.core.mail import send_mass_mail
# Create your views here.


def send_email(request):
    # for user in User.objects.all():


    # send_mass_mail('Another Subject', 'Here is another message', 'from@example.com',  ['john@example.com', 'jane@example.com'], fail_silently=False)
    if request.method == "POST":
        email = request.POST.get("email")
    #     subject = request.POST.get('subject')
    #     # for user in User.objects.all():
        send_email("subject oes here", "message goes here", 'no-reply-oketofoke@gmail.com', [email])
        return HttpResponse('sending message')
    return render (request, 'emails/Send_Emails.html')


# for user in Users.objects.all():
#     send_mail(subject, message, from_email,
#         user.Email)