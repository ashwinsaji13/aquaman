from django.conf.urls import url, include
from django.urls import path
# rest-framework
from rest_framework.routers import DefaultRouter

# custom imports
from .views import *

router = DefaultRouter()
# api/users
router.register('users', AccountViewSet, base_name='users')

urlpatterns = [
 path('api/', include(router.urls)),
 # login
 path('login/', Login.as_view()),
 # for registering users
 path('register', UserRegister.as_view())
]