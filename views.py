from django.shortcuts import render
from .models import Product
from product.models import Post
from .models import Register, Signin


def contact(request):
    return render(request, "contact.html")


from product.forms import ProductForm


def products(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:

                form.save()
                return render(request, "feedback.html")
            except:
                pass
    else:

        form = ProductForm()
        print("bye")
    return render(request, "index.html", {'form': form})


from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # get a cursor object from the database connection
        cursor = connection.cursor()

        # my_query is a string with the SQL you want executed
        cursor.execute(
            "Select * from shopperstoppe.users where username = '" + username + "' and password = '" + password + "'")
        data = cursor.fetchone()
        if (data is None):
            return render(request, 'login.html', {'context': 'Username and password incorrect!!'})
        else:
            return render(request, 'home.html')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def show(request):
    product = Product.objects.all()
    return render(request, "show.html", {'pdt': product})


def registration(request):
    return render(request, "registration.html")


# inserting in html


def feedback(request):
    if request.method == 'POST':
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get(
                'email') and request.POST.get('country') and request.POST.get('feedback'):
            post = Post()
            post.firstname = request.POST.get('firstname')
            post.lastname = request.POST.get('lastname')
            post.email = request.POST.get('email')
            post.country = request.POST.get('country')
            post.feedback = request.POST.get('feedback')

            post.save()
            '''if post.fname != post.lname != post.email != post.country != post.feedback:
                return render(request, 'login.html', {'context': 'password and confirm_password does not match'})
                post.save()'''

            return render(request, 'home.html')

    else:
        return render(request, 'feedback.html')


# registration form
def home(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('contact') and request.POST.get('email') and request.POST.get(
                'psw') and request.POST.get('psw_repeat'):
            container = Register()
            container.title = request.POST.get('name')
            container.content = request.POST.get('contact')
            container.content = request.POST.get('email')
            container.content = request.POST.get('psw')
            container.content = request.POST.get('psw_repeat')

            container.save()
            '''if container.name != container.contact != container.email != container.psw != container.psw_repeat:
                return render(request, 'login.html', {'context': 'password and confirm_password does not match'})
                container.save()'''

            return render(request, 'show.html')

    else:
        return render(request, 'home.html')


# signin form
def signin(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            cursor = connection.cursor()

            # my_query is a string with the SQL you want executed
            cursor.execute(
                "Select * from engine.signin where username = '" + username + "' and password = '" + password + "'")
            data = cursor.fetchone()
            if (data is None):
                return render(request, 'signin.html', {'context': 'Username and password incorrect!!'})
            else:
                return render(request, 'feedback.html')
    else:
        return render(request, 'signin.html')


# signout form
def signout(request):
    if request.method == 'POST':
        if request.POST.get('firstname') and request.POST.get('email') and request.POST.get(
                'address') and request.POST.get('city') and request.POST.get('state') and request.POST.get(
            'zip') and request.POST.get('card_name') and request.POST.get('card_number') and request.POST.get(
            'exp_month') and request.POST.get('exp_year') and request.POST.get('cvv'):
            post = Post()
            post.firstname = request.POST.get('firstname')
            post.email = request.POST.get('email')
            post.address = request.POST.get('address')
            post.city = request.POST.get('city')
            post.state = request.POST.get('state')
            post.zip = request.POST.get('zip')
            post.card_name = request.POST.get('card_name')
            post.card_number = request.POST.get('card_number')
            post.exp_month = request.POST.get('exp_month')
            post.exp_year = request.POST.get('exp_year')
            post.cvv = request.POST.get('cvv')

            post.save()
            '''if post.fname != post.email != post.adr != post.city != post.state != post.zip != post.cname != post.ccnum != post.expmonth != post.expyear != post.cvv:
                return render(request, 'login.html', {'context': 'password and confirm_password does not match'})
                post.save()'''

            return render(request, 'home.html')

    else:
        return render(request, 'signout.html')


# add to cart

def cart(request):
    if request.method == 'POST':
        if request.POST.get('cart_items') and request.POST.get('counter') and request.POST.get(
                'prices') and request.POST.get('items') and request.POST.get('total_amount') and request.POST.get(
                'amount') and request.POST.get('save') and request.POST.get('remove'):
            post = Post()
            post.cart_items = request.POST.get('cart_items')
            post.counter = request.POST.get('counter')
            post.prices = request.POST.get('prices')
            post.items = request.POST.get('items')
            post.total_amount = request.POST.get('total_amount')
            post.amount = request.POST.get('amount')
            post.subtotal = request.POST.get('subtotal')
            post.save = request.POST.get('save')
            post.remove = request.POST.get('remove')

            post.save()
            '''if post.cart_items != post.counter != post.prices != post.items != post.total_amount !=  post.amount != 
            post.save != post.remove != post.subtotal :
                return render(request, 'login.html', {'context': 'password and confirm_password does not match'})
                post.save()'''

            return render(request, 'home.html')

    else:
        return render(request, 'cart.html')
