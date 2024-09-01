from django.db import models

from django.utils import timezone


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
    


    
    
    
    
    


    
    
    
    
    
    
    
    
    
    
    
    
