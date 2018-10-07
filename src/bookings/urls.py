from django.conf.urls import url, include
from django.urls import path
from .views import BookingsView, BookingsUploadView, ContainersView, TrialPageViewSet
from rest_framework_nested import routers


router = routers.SimpleRouter()
router.register('bookings-uploads', BookingsUploadView, base_name='bookings-uploads'),
router.register('bookings', BookingsView, base_name='bookings')
router.register('containers', ContainersView, base_name='containers')
router.register('try-page', TrialPageViewSet, base_name='try-page')

urlpatterns = [
    path('api/', include(router.urls))
]