from typing import ContextManager
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.



def product_view(request):
    form = ProductForm(request.POST or None) # if post req then fill with form data or just return a blank form
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('create')
    context = {
       'form' : form
    }
    return render(request, "create.html", context)
# The form variable is used to initialize the django form to the database.
# Essentially acts as bridge between the database and webpage.
# If the form is valid, then we save it and refresh the page, without form resubmission.


def product_edit(request):
    productId = 33 #variable for user
    obj = Product.objects.get(id=productId) #gets the product
    form = ProductForm(request.POST or None, instance=obj) #renders the form with the given product
    if form.is_valid():
        form.save() #updates product
        return HttpResponseRedirect('edit')
    context = {
       'form' : form
    }
    return render(request, "edit.html", context)
# needs modification to make url dynamic

def product_view_1(request):
    if request.method == 'POST':
        myTitle = request.POST.get('title')
        myPrice = request.POST.get('price')
        myDescription = request.POST.get('description')
        Product.objects.create(title=myTitle, price=myPrice, description=myDescription)
        return HttpResponseRedirect('create1')
    context = {}
    return render(request, "create(1).html", context)
# If it is a POST request, the title, price and description are transferred to the variables made.
# Then creates a model object and re-renders the page. 
# It is difficult to maintain data integrity using this process.


def product_view_2(request):
    initial_data = {
        "price" : "13.99"
    }
    rawForm = RawProductForm(initial=initial_data) #sets the initial value of a field
    if request.method == 'POST':
        rawForm = RawProductForm(request.POST)
        if rawForm.is_valid():
            print(rawForm.cleaned_data)
            Product.objects.create(**rawForm.cleaned_data) #creates a product
            return HttpResponseRedirect('create2')
        else:
            print(rawForm.errors)    #if it fails it prints the errors
    context = {
        'form' : rawForm
    }
    return render(request, "create(2).html", context)


def product_detail(request):
    obj = Product.objects.get(id=1)
    context = {
        'object' : obj,
    }
    return render(request, "details.html", context)
# Importing Product model, then using the product_detail function to render out data
# from the Product model objects (in the database), using django's builtin ID assignment system.
# Context dict is used to assign a key to the variable obj, so as to function inside the template.

def product_dynamic_lookup_view(request, my_id): #takes my_id from url link
    obj = get_object_or_404(Product, id=my_id) 
    # inbuilt function uses model.objects.get(model=Model,id=x) and returns a 404 incase unavailable
    
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404
    # same as the above but using a try-except block

    if request.method=='POST': # upon form submission 
        obj.delete() # deletes the object
        return redirect(f'../{my_id + 1}') #redirects to next object detail page using f strings
    context={
        'object': obj
    }
    return render(request, "details(2).html", context)


def product_home(request):
    queryset = Product.objects.all() #returns the list of objects or instances
    context = {
        'object_list' : queryset #standard naming used for reusablity
    }
    return render(request, "product_home.html", context)
