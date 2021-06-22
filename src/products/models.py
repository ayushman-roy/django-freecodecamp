from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    title       = models.CharField(max_length = 100)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    summary     = models.TextField(blank=True)
    featured    = models.BooleanField(null=True)

    def get_absolute_url(self):
        return reverse("products:product details via dyanmic urls", kwargs={"my_id": self.id})
    # function used to redirect to a page (app_name:page_name) using kwargs as needed. 
    # dynamic form of url routing where it takes the instance data and uses it to route as needed
    # here it takes instance id and passes it into the page view with the given name
    
    def get_absolute_url_beta(self):
        return f'/product/detail1/{self.id}'
    # hardcoding the get_absolute_url function 
    # uses f strings to get the instance data and pass it into the url
    # not recommended as it is not very adaptive and can return a lot of errors
    