from .models import Category

def global_categories(request):
    return {
        'nav_categories': Category.objects.all()
    }
