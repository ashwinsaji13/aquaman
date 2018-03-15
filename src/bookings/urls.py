from django.conf.urls import url, include
from django.urls import path
from .views import BookingsView
from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register('bookings', BookingsView, base_name='bookings')

urlpatterns = [
    path('api/', include(router.urls))
]