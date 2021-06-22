from typing import ItemsView
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Keep your logic inside the views and keep the rendering inside the templates.

def home_view(requests,*args, **kwargs):
    print(requests.user)
    print(*args, **kwargs)
    return HttpResponse("<h1> This is my first django homepage!</h1>")

def contact_view(requests, *args, **kwargs):
    return render(requests, template_name="contact.html")

def about_view(requests, *args, **kwargs):
    myContext = {
        "myTitle"  : "practice project",
        "myText"   : "normal testing",
        "myNumber" : 123,
        "myValue"  : True, 
        "myList"   : ['burger', 'pizza', 'calzones', 124566, False]
    }

    value = myContext['myList']
    count = 0
    for item in value:
        myContext['Item'+str(count)] = item
        count += 1
    # Above block of code - 
    # Takes the data stored in the myList key, and assigns a var to it. Also count created for loop purposes.
    # For loop initiated, where for each item in value, a new dict key (Item + Loop Count = Item0) is created.
    # That key is assigned data from the value list, as per index. Count incremented each loop to avoid variable clashes.
    # We will rarely use for-loops like this, because of clutter and code-maintaining issues.

    return render(requests, "about.html", myContext)
    # The render function mashes the template and context together, and renders out the required. 
    # Think of context as a reference unit.


