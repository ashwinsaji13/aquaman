import threading
import hashlib
from django.core.mail import EmailMultiAlternatives

# custom imports
from .models import Account


LINK = 'http://139.59.72.184/'
DEMO_MANAGER = 'manager.vja@gmail.com'


def send_simple_message(subject, body, from_mail, recipient_list, html=None):
    """
    Email sending with text and template in the body.
    """
    subject, from_email, to = subject, from_mail, recipient_list
    text_content = body
    html_content = html
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    if html:
        msg.attach_alternative(html_content, "text/html")
    msg.content_subtype = "html"
    msg.send()


class EmailThread(threading.Thread):

    def __init__(self, subject, body, from_email, recipient_list,
                 fail_silently, html):
        self.subject = subject
        self.body = body
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.html = html
        threading.Thread.__init__(self)

    def run(self):
        if self.html is None:
            send_simple_message(self.subject, self.body, self.from_email,
                                self.recipient_list)
        else:
            send_simple_message(self.subject, self.body, self.from_email,
                                self.recipient_list, html=self.html)


def thread_mail(subject, body, from_email, recipient_list,
                fail_silently=False, html=None, *args, **kwargs):
    EmailThread(subject, body, from_email, recipient_list, fail_silently,
                html).start()


def reset_password(email):
    """
    Method for sending email for resetting the password
    """
    subject = 'Password Reset-TASS'
    email = email.encode('utf-8')
    key = settings.SECRET_KEY.encode('utf-8')
    hash_object = hashlib.sha512(email+key)
    key = hash_object.hexdigest()
    account_id = Account.objects.get(email=email).id
    link = ''.join([LINK, 'reset_password/', str(account_id), '/', key])

    message = 'Reset Link'
    html = '''<p>Please click on the <strong>link</strong> below to reset your password for VJA.</p>
        <br>Reset link : <a href="{0}">{0}</a>'''.format(link)
    from_mail = DEMO_MANAGER
    mail_list = [email]

    thread_mail(subject, message, from_mail, mail_list, fail_silently=False,
                html=html)
