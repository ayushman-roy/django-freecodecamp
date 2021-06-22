from django.urls import path
from products.views import product_detail, product_view, product_view_1, product_view_2, product_edit, product_dynamic_lookup_view, product_home
# seperating app urls from project url file for reusablity
# standard practice to make seperate url files and link them to the project url files via include

app_name = 'products'
# giving namespace to page names, for easy referencing in functions like get_absolute_url
# also makes it heavily reusable

urlpatterns = [
    path('detail/', product_detail, name= 'product details'),
    path('create/', product_view, name='create product'),
    path('create1/', product_view_1, name='create product via HTML'),
    path('create2/', product_view_2, name='create product via raw django'),
    path('edit/', product_edit, name='update product details'),
    path('detail1/<int:my_id>/', product_dynamic_lookup_view, name='product details via dyanmic urls'),
    path('', product_home, name='product home')
]

# backslash at end of urls is important as without that we get a 404
# part of django rule for url readablity 

# no 'product' at start of url names as it is already included from the main url file
# all urls here are relative to the app products