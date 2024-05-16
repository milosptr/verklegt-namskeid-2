from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string

from src.controllers.GeneralViewController import GeneralViewController
from src.models.user import User


class EmailController:
    @staticmethod
    def contact_us(request):
        if request.method == 'POST':
            subject = 'Jarvis contact form'
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            email_from = request.POST.get('email')
            recipient_list = ['jarvisvk2@gmail.com']
            msg_html = render_to_string('email/contact_form.html', {
                'name': name,
                'email': email,
                'phone': phone,
                'message': request.POST.get('message')

            })

            msg_plain = 'Contact form from Jarvis: \n' + 'Name: ' + name + '\n' + 'Email: ' + email + '\n' + 'Phone: ' + phone + '\n' + 'Message: ' + request.POST.get(
                'message')

            send_mail(subject, msg_plain, email_from, recipient_list, html_message=msg_html)
            messages.success(request, 'Successfully nonono')
            return redirect('/contact-us')
        else:
            return GeneralViewController(request).render('pages/contact_us.html')

    @staticmethod
    def reset_password(request):
        if request.method == 'POST':
            email = request.POST.get('email')
            user = User.get_by_email(email)
            if not user:
                messages.error(request, 'Email does not exist')
                return redirect('/forgot-password')

            password = user.reset_password()
            subject = 'Jarvis: Password reset request'
            recipient_list = [email]
            msg_plain = 'Your new password is: ' + password
            msg_html = render_to_string('email/reset_password.html', {
                'password': password
            })

            send_mail(subject, msg_plain, 'jarvisvk2@gmail.com', recipient_list, html_message=msg_html)
            messages.success(request, 'Password has been reset. Check your email')
            return redirect('/login')
        else:
            messages.error(request, 'An error occurred. Please try again')
            return redirect('/forgot-password')
