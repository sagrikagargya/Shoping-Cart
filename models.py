from django.db import models

class Product(models.Model):
    pname = models.CharField(max_length=255)
    cost=models.CharField(max_length=20)
    description=models.CharField(max_length=100)
    discount=models.IntegerField()
    img=models.CharField(max_length=2083)

    class Meta:
        db_table = "product"




# Create your models here.
class UsersModel(models.Model):
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    contact = models.IntegerField(max_length=100)
    address= models.CharField(max_length=250)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "users"
#for direct html page
class Post(models.Model):
    firstname= models.CharField(max_length=250, unique=True)
    lastname= models.TextField()
    email=models.CharField(max_length=250)
    country=models.CharField(max_length=250)
    feedback=models.TextField()

    class Meta:
        db_table = "feedback"

class Register(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password= models.CharField(max_length=250)
    repeatpasssword = models.CharField(max_length=100)

    class Meta:
        db_table = "register"

class Signin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


    class Meta:
        db_table = "signin"

class Signout(models.Model):
    firstname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    card_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)
    exp_month = models.CharField(max_length=100)
    exp_year = models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)



    class Meta:
        db_table = "signout"

 #add products to cart
class Cart(models.Model):
    cart_items = models.CharField(max_length=100)
    counter = models.CharField(max_length=100)
    prices = models.CharField(max_length=100)
    items = models.CharField(max_length=100)
    total_amount = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    subtotal = models.CharField(max_length=100)
    save = models.CharField(max_length=100)
    remove = models.CharField(max_length=100)




    class Meta:
        db_table = "cart"

