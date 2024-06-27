# Create the custom user mode 
from functools import wraps
from django.core.exceptions import PermissionDenied
from .models import *

def get_user_role(user):
    try:
        user_role = UserRole.objects.get(user__id=user.id)
        return user_role.role
    except UserRole.DoesNotExist:
        return None

def has_permission(permission_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated:
                user_role = get_user_role(request.user)
                if user_role and user_role.permissions.filter(name=permission_name).exists():
                    return view_func(request, *args, **kwargs)
            raise PermissionDenied("You don't have permission to access this page.")
        return _wrapped_view
    return decorator