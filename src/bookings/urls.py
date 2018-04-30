from django.conf.urls import url, include
from django.urls import path
from .views import BookingsView, BookingsUploadView, ContainersView
from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register('bookings-uploads', BookingsUploadView, base_name='bookings-uploads'),
router.register('bookings', BookingsView, base_name='bookings')
router.register('containers', ContainersView, base_name='containers')


urlpatterns = [
    path('api/', include(router.urls))
]