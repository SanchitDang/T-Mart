from django.shortcuts import render,redirect
from products.forms import *
from products.models import *

from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from store.settings import API_KEY, AUTH_TOKEN
from django.contrib.auth import authenticate, login as loginUser


def admin_login(request):
    if not request.user.is_superuser and  not request.user.is_staff:
        return redirect('admin_login')
    if request.method == 'GET':
        form = Adminloginform() #This comes from forms.py
        context = {'form':form}
        return render(request, 'webadmin/admin_login.html', context)
    else:
        form = Adminloginform(data=request.POST) #This comes from forms.py
        if form.is_valid():
            username = form.cleaned_data.get('username')    
            password = form.cleaned_data.get('password')    
            user = authenticate(username=username, password=password)
            if user:
                loginUser(request, user) 
            messages.success(request, "Welcome Admin")  
            return redirect('admin_dashboard')    
        else:
            context = {'form':form}
            return render(request, 'webadmin/admin_login.html', context)


@login_required(login_url='admin_login')
def admin_dashboard(request):
    if not request.user.is_superuser and  not request.user.is_staff:
        return redirect('admin_login')

    tshirtcount = product.objects.all().count()
    ordercount = order.objects.all().count()
    usercount = User.objects.all().count()
    context = {'tshirtcount':tshirtcount, 'order':ordercount, 'user':usercount}
    return render(request, 'webadmin/index.html', context)

@login_required(login_url='admin_login')
def all_users(request):
    if not request.user.is_superuser and  not request.user.is_staff:
        return redirect('admin_login')
    allusers = User.objects.all()
    context = {'allusers':allusers}
    return render(request, 'webadmin/users.html', context) 


@login_required(login_url='admin_login')
def all_orders(request):
    if not request.user.is_superuser and  not request.user.is_staff:
        return redirect('admin_login')
    allorders = order.objects.all()
    context = {'allorders':allorders}
    return render(request, 'webadmin/orders.html', context) 


@login_required(login_url='admin_login')
def all_products(request):
    if not request.user.is_superuser and  not request.user.is_staff:
        return redirect('admin_login')
    all_prod = product.objects.all()
    context = {'prod':all_prod}
    return render(request, 'webadmin/products.html', context)


@login_required(login_url='admin_login')
def add_product(request):
    if not request.user.is_superuser and  not request.user.is_staff:
        return redirect('admin_login')
    productForm= ProductForm()
    productsizeForm = ProductsizeForm()
    if request.method=='POST':
        productForm=ProductForm(request.POST, request.FILES)
        productsizeForm=ProductsizeForm(request.POST, request.FILES)
        if productForm.is_valid() and productsizeForm.is_valid():
            a = productForm.save()
            b = productsizeForm.save(commit=False)
            b.foreignkeytoA = a
            b.save()
        return redirect('all_products')
    return render(request, "webadmin/add_product.html", {'product':productForm, 'productsizeForm':productsizeForm})



@login_required(login_url='admin_login')
# Add Product and it's Types by Custom Admin Panel
def add_brand(request):
    if not request.user.is_superuser and  not request.user.is_staff:
        return redirect('admin_login')
    brand= brandform()
    if request.method=='POST':
        brand=brandform(request.POST, request.FILES)
        if brand.is_valid():
            brand.save()
        messages.success(request, "Brand Added Sucessfully !!")    
        return redirect('all_products')
    return render(request, "webadmin/brand.html", {'brand':brand})


@login_required(login_url='admin_login')
def add_occassion(request):
    if not request.user.is_superuser and  not request.user.is_staff:
        return redirect('admin_login')
    occassion= Occassionform()
    if request.method=='POST':
        occassion=Occassionform(request.POST, request.FILES)
        if occassion.is_valid():
            occassion.save()
        messages.success(request, "Occassion Added Sucessfully !!")    
        return redirect('all_products')
    return render(request, "webadmin/occassion.html", {'occassion':occassion})


@login_required(login_url='admin_login')
def add_color(request):
    if not request.user.is_superuser and  not request.user.is_staff:
        return redirect('admin_login')
    color= colorform()
    if request.method=='POST':
        color=colorform(request.POST, request.FILES)
        if color.is_valid():
            color.save()
        messages.success(request, "color Added Sucessfully !!")    
        return redirect('all_products')
    return render(request, "webadmin/color.html", {'color':color})


@login_required(login_url='admin_login')
def add_neck(request):
    if not request.user.is_superuser and  not request.user.is_staff:
        return redirect('admin_login')
    neck= neckform()
    if request.method=='POST':
        neck=neckform(request.POST, request.FILES)
        if neck.is_valid():
            neck.save()
        messages.success(request, "neck Added Sucessfully !!")    
        return redirect('all_products')
    return render(request, "webadmin/neck.html", {'neck':neck})


@login_required(login_url='admin_login')
def edit_product(request, id):
    if not request.user.is_superuser and  not request.user.is_staff:
        return redirect('admin_login')
    if request.method == 'POST':
        tshirt = product.objects.get(id=id)
        editproductForm= EditproductForm(request.POST, instance=tshirt)
        if editproductForm.is_valid():
            editproductForm.save()
        messages.success(request, "Product Update Sucessfully !!")
        return redirect('all_products')
    else:
        tshirt = product.objects.get(id=id)
        editproductForm= EditproductForm(instance=tshirt)

    return render(request, "webadmin/edit_product.html", {'editproduct':editproductForm})


@login_required(login_url='admin_login')
def delete_product(request, id):
    if not request.user.is_superuser and  not request.user.is_staff:
        return redirect('admin_login')
    delete = product.objects.get(pk=id)  #pk means primary key
    delete.delete()
    messages.success(request, "Product Deleted Successfully.")
    
    return redirect('all_products')