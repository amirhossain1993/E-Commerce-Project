from main_app.models import Category


def global_category(request):
    global_category = Category.objects.all()
    return {
        'global_category': global_category
    }