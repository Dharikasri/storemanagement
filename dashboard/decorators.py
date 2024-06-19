from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME

def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='dashboard:login_view'):
    """
    Decorator for views that checks that the user is logged in and is an admin,
    redirecting to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_superuser or u.groups.filter(name='Admin').exists(),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
