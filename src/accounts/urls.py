from django.conf.urls import url, include
from django.urls import path, re_path
# rest-framework
from rest_framework.routers import DefaultRouter

# custom imports
from .views import AccountViewSet, Login, UserRegister, ForgotPassword, ResetPassword

router = DefaultRouter()
# api/users
router.register('users', AccountViewSet, base_name='users')

urlpatterns = [
    path('api/', include(router.urls)),
    # login
    path('login/', Login.as_view()),
    # for registering users
    path('register', UserRegister.as_view()),
    # forgot password and reset password
    path('forgot_password', ForgotPassword.as_view()),
    re_path('reset_password/(?P<pk>\d+)/(?P<key>[-\w\d]+)', ResetPassword.as_view())
    # path('reset_password', ResetPassword.as_view())
]

