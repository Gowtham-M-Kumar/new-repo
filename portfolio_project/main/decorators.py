from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def admin_required(view_func):
    """
    Custom decorator to check if user is authenticated as admin
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.session.get('admin_authenticated'):
            messages.error(request, 'Please log in to access this page.')
            return redirect('settings_login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view 