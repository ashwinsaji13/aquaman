

# rest_framework
from rest_framework.permissions import BasePermission


class AdminOnlyListPermission(BasePermission):
    """
    Only admin can list the objects. But the owner can view their own objects.
    Mainly used for users list.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated():
            return False
        if view.action in ['retrieve', 'update', 'list']:
            return True
        return request.user.is_admin

    def has_object_permission(self, request, view, obj):
        try:
            return request.user.is_admin or getattr(obj, view.user_lookup_kwarg) == request.user
        except AttributeError:
            return request.user == obj
        except:
            pass
        return request.user.is_admin
