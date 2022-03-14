from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TrendingProduct(models.Model):
    image = models.ImageField(upload_to= 'pics')
    status = models.IntegerField(blank= True, null= True )
    description = models.CharField(max_length= 70)
    old_price = models.FloatField()
    new_price = models.FloatField()
    name = models.CharField(max_length=20)
    shipping = models.BooleanField(default=False, null= True, blank= True)

    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField(upload_to= 'pics')
    description = models.CharField(max_length= 70)
    price = models.FloatField()
    name = models.CharField(max_length=20)
    shipping = models.BooleanField(default=False, null= True, blank= True)

    def __str__(self):
        return self.name

class Testimony(models.Model):
    POSITION = (
        ('C', 'Customer'),
        ('S', 'Staff'),
    )
    image = models.ImageField(upload_to= 'pics')
    testimony = models.TextField()
    name = models.CharField(max_length= 30)
    position = models.CharField(max_length = 10, choices=POSITION)
    

    def __str__(self):
        return self.name

class Shop(models.Model):
    image = models.ImageField(upload_to= 'pics')
    status = models.CharField(blank= True, null= True,max_length=500 )
    description = models.CharField(max_length= 70)
    old_price = models.FloatField()
    new_price = models.FloatField()
    shipping = models.BooleanField(default=False, null= True, blank= True)
    
    def __str__(self):
        return self.description

class ShopDetails(models.Model):
    shop = models.ForeignKey(Shop, default=1, on_delete= models.SET_DEFAULT)
    short_desc = models.TextField(max_length= 100)
    full_desc = models.TextField(max_length= 400)

    def __str__(self):
        return self.short_desc

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null= True)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null= True, blank= True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200, null= True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.shop.shipping == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    trendingproduct = models.ForeignKey(TrendingProduct, on_delete=models.SET_NULL, null= True, blank= True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null= True, blank= True)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null= True, blank= True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null= True, blank= True)
    quantity= models.IntegerField(blank= True,null= True,default=0)
    date_added= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.shop.description

    @property
    def get_total(self):
        total = self.shop.new_price * self.quantity
        return total

class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null= True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null= True)
    address = models.CharField(max_length=200, null= True)
    city = models.CharField(max_length=200, null= True)
    states = models.CharField(max_length=200, null= True)
    zipcode = models.CharField(max_length=200, null= True)
    date_added = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.address