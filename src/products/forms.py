from django import forms
from .models import Product
# Imports forms class templates and the user-made Model.

class ProductForm(forms.ModelForm): # ProductForm class inherits from the ModelForm class.
    title       = forms.CharField(
                        required=True, 
                        max_length=30,
                        widget=forms.TextInput(
                            attrs={
                            "placeholder" : "Enter Your Product Name"
                        })) # overrides the formatting in fields
    class Meta:
        model = Product
        fields = [
            'title', 
            'description',
            'price'
        ] # Meta class is used to initalize the model and fields objects inside the class.
    def clean_description(self, *args, **kwargs): #use args if you are unsure if any overidden
        description = self.cleaned_data.get("description") #gets the description of the instance
        title = self.cleaned_data.get("title")
        if not str(title) in description: 
            raise forms.ValidationError("Your Product Name must be in the Description!") 
        return description #validation of data


class RawProductForm(forms.Form): #pure django form
    title       = forms.CharField(
                        required=True, 
                        initial="Product",
                        max_length=30) #form formatting, adding fields
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                            attrs={
                                "class" : "this-is-for-CSS multiple-classes",
                                "cols" : "30",
                                "rows"   : "20"
                            }))
    price       = forms.DecimalField(
                        widget=forms.TextInput(
                            attrs={
                                "placeholder" : "19.99"
                            }))
# widget basically is used to format the form as per need. charfield is for initializing a field.
# while textarea is for formatting in forms.
# these are called form fields.
