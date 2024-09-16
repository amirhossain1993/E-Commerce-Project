from main_app.models import *


def global_category(request):
    global_category = Category.objects.all()
    return {
        'global_category': global_category
    }
    
    
def global_cart(request):
    cart = Cart.objects.count()
    return {'cart':cart}


def global_wishlistt(request):
    wishlist = Wishlist.objects.count()
    return {'wishlist':wishlist}