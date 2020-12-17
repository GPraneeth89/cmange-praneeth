from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    Phone=models.CharField(max_length=25, null=True)
    email=models.EmailField(max_length=254 , null= True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name +"  |  "+ self.Phone + "  |  "+self.email
        
class Tags(models.Model):
    name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor')
    )
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=20,null=True ,choices=CATEGORY)
    description=models.CharField(max_length=300,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    tags=models.ManyToManyField(Tags)


    def __str__(self):
        return self.name


    
class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered')
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    
    def __str__(self):
        return self.product 




