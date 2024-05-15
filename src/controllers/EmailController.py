from django.shortcuts import redirect
from django.core.mail import send_mail

class EmailController:
  @staticmethod
  def contact_us(request):

    subject = 'Jarvis contact form'
    message = request.POST.get('message')
    email_from = request.POST.get('email')
    recipient_list = 'alexia22@ru.is'
    send_mail( subject, message, email_from, recipient_list )
    return redirect('/contact-us')
