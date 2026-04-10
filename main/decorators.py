from functools import wraps

from .models import Category


def navbar_preload():
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            categories = Category.objects.all()
            result = func(*args, **kwargs)
            result['categories'] = categories
            return result
        return wrapper
    return deco

