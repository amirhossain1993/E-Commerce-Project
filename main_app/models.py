from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User


# Create your models here.

# Contact Model

class ContactInfo(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    subject = models.CharField(max_length=450)
    message = models.TextField()

    class Meta:
        verbose_name_plural ="Contact Informations"

    def __str__(self):
        return self.name + '' + self.subject  
    



#Product Model

class Banner(models.Model):
    name = models.CharField (max_length=300)
    image = models.ImageField (upload_to='bannar_image/')
    product_name = models.CharField (max_length=400,null=True, blank=True)
    price = models.CharField (max_length=14)
    discount_price = models.CharField (max_length=14)
    
    class Meta:
        verbose_name_plural =("Banners")
    
    def __str__(self):
        return self.name
    
    
    
#Category Model

class Category(models.Model):
    name = models.CharField (max_length=50, null=False)
    image = models.ImageField (upload_to='category_image/', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural =("Categorys")
    
    def __str__(self):
        return self.name
    
    
    
    
#Brand Model

class Brand(models.Model):
    name = models.CharField (max_length=50, null=False)
    image = models.ImageField (upload_to='category_image/', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural =("Brands")
    
    def __str__(self):
        return self.name
    



#Products Model

class Product(models.Model):
    name = models.CharField (max_length=200)
    image = models.ImageField (upload_to='product_image/')
    # product_side_image = models.ImageField (upload_to='product_side_image/')
    # product_cross_image = models.ImageField (upload_to='product_cross_image/')
    # product_with_model_image = models.ImageField (upload_to='product_with_model_image/')
    # product_back_image = models.ImageField (upload_to='product_back_image/')
    regular_price = models.PositiveIntegerField()
    discount_price = models.PositiveSmallIntegerField(blank=True, null=True)
    descriptions = models.TextField()
    aditional_descriptions = models.TextField()
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural =("Products")
    
    def __str__(self):
        return self.name
    
    
    
# Cary and  Wishlist and Order Models
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
    
    
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s Wishlist - {self.product.name}"
    

class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    items = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order {self.id} - {self.user.username}"
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Order {self.product.name} - {self.quantity}"
    


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    delivery_area = models.CharField(max_length=20, choices=[('inside_dhaka', 'Inside Dhaka'), ('outside_dhaka', 'Outside Dhaka')])
    
    def _str_(self):
        return f"{self.user.username} - {self.address}"


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    )
    
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Payment for Order {self.order.id}"
    

    
    
    
