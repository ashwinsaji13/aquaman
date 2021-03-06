import hashlib

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import password_reset
from django.shortcuts import HttpResponseRedirect

# rest_framework
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, IsAdminUser, IsAuthenticated

# custom imports
from .mails import reset_password
from .models import Account
from .serializers import AccountSerializer


# Create your views here.
def user_logout(request):
    """
    Logs out the current user.
    """
    logout(request)
    return HttpResponseRedirect('/')


class Login(APIView):
    """
    Front end authentication is via tokens. This class generates an authentication
    token for the user
    """
    permission_classes = []

    def post(self, request):
        """
        Token request method must be POST.
        """

        success = 'false'
        msg = "Error while logging in"
        token = None
        user = user_id = None
        name = ""
        try:
            email = request.data['email'].strip().lower()
            password = request.data['password'].strip()
            user = authenticate(email=email, password=password)
            if user:
                success = 'true'
                tok, created = Token.objects.get_or_create(user=user)
                user_id = tok.user_id
                token = tok.key
                msg = "User Authenticated"
                name = user.full_name
            else:
                msg = "Error in User Credentials Provided."
            # superu = Account.objects.get(email=email)

        except Exception as e:
            msg = str(e)
        return Response({
            'msg': msg,
            'success': success,
            'token': token,
            'name': name,
            'user': user_id,
            'admin': user.admin if user else None,
            'initial_login': user.initial_login if user else False
        })


class ForgotPassword(APIView):
    """
    Class to take action when a client user forgets his/her password.
    """

    permission_classes = []

    def post(self, request):
        """
        Request for Password Reset must be POST.
        """
        success = False
        msg = "Unknown Error"
        account = None
        try:
            email = request.data['email']
            try:
                account = Account.objects.get(email=email)
            except:
                msg = "No such User"
            if account:
                reset_password(email)
                success = True
                msg = "Email sent. Please check your inbox"

        except Exception as e:
            msg = str(e)
        return Response({
            'msg': msg,
            'success': success,
        })


class ResetPassword(APIView):
    """
    View provided for requesting a password reset.
    """

    permission_classes = []

    def get(self, request, *args, **kwargs):
        """
        No GET request.
        """
        return Response({})

    def post(self, request, pk, key):
        """
        POST request accepts arguments 'new_password'.
        Query Parameters must contain unique id and hash key.
        """
        success = False
        msg = "Unknown Error"
        try:
            new_password = request.data['new_password']
            account = Account.objects.get(pk=pk)
            email = account.email.encode('utf-8')
            secret_key = settings.SECRET_KEY.encode('utf-8')
            hash_key = hashlib.sha512(email + secret_key).hexdigest()
            if hash_key == key:
                account.set_password(new_password)
                account.save()
                msg = "Password Updated"
                success = True
            else:
                success = False
                msg = "Invalid / Expired Key"

        except Exception as e:
            msg = str(e)
        return Response({
            'msg': msg,
            'success': success,
        })


class ChangePasswordView(APIView):
    """
    View for requesting a password change from the logged in account.
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """
        POST request accepts current_password and new_password as parameters and set the new password.
        """
        success = False
        msg = "Unknown Error"
        try:
            user = request.user
            current_password = request.data['current_password']
            new_password = request.data['new_password']
            if user.check_password(current_password):
                user.set_password(new_password)
                user.initial_login = False
                user.save()
                msg = "Password has been successfully Updated."
                success = True
            else:
                msg = "Please provide your current password."
        except Exception as e:
            msg = str(e)
        return Response({
            'success': success,
            'msg': msg,
        })


class AccountViewSet(viewsets.ModelViewSet):
    """
    View for accessing User details.
    Provides 'list', 'retrieve', 'create', 'update' & 'delete' methods.
    Permission level only for partners/HR.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def list(self, request):
        return super(AccountViewSet, self).list(request)


class UserRegister(APIView):
    """
    for registering users
    """
    permission_classes = []

    def post(self, request):
        success = 'false'
        msg = "user not registered"

        try:
            email = request.data['email']
            password = request.data['password']
            full_name = request.data['full_name']
            phone_number = request.data['phone_number']

            user = Account.objects.create_user(email=email, password=password, full_name=full_name, \
                                               phone_number=phone_number, staff=True)
            if user:
                success = 'true'
                msg = 'User Created'
                user.save()
            else:
                msg = 'User has not been created.Please register again!!!!'

        except:
            msg = "The user is already registered. Please sign in from the Login page"
        return Response({
            'msg': msg,
            'success': success
        })
