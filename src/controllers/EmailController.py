from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages
from src.controllers.GeneralViewController import GeneralViewController

class EmailController:
  @staticmethod
  def contact_us(request):
    if request.method == 'POST':
      subject = 'Jarvis contact form'
      message = request.POST.get('message')
      email_from = request.POST.get('email')
      recipient_list = ['jarvisvk2@gmail.com']

      send_mail(subject, message, email_from, recipient_list)
      messages.success(request, 'Successfully nonono')
      return redirect('/contact-us')
    else:
        return GeneralViewController(request).render('pages/contact_us.html')
