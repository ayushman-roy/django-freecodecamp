from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .models import Journal
from .forms import JournalForm
# Create your views here.

class ClassBasedListView(View):
    template_name = "journal_list.html"
    queryset = Journal.objects.all()
    def get_queryset(self):
        return self.queryset
        # makes the view more adaptable, easy modifications to the passed queryset and seamless inheritence
    def get(self, request, *args, **kwargs):
        # handles the GET requests
        context={
            'object_list': self.get_queryset()
        }
        return render(request, self.template_name, context) 

def FunctionBasedListView(request):
    queryset = Journal.objects.all()
    context={
        'object_list': queryset
    }
    return render(request, "journal_list.html", context) 

# both views above are equivalent 
# function based view -> class based view, by nesting it inside a class and configuring for a get request
# class based views allows for easy maintenance, resuablity and adaptability 

class GetObjectMixin(object):
    model = Journal # the required object's model
    lookup = "id" # lookup type as per url
    def get_object(self, *args, **kwargs):
        lookup = self.kwargs.get(self.lookup) # gets the value of the lookup
        obj = None
        if lookup is not None:
            obj = get_object_or_404(self.model, id=lookup) 
            # grabs the object via the lookup value, can change id to other fields like title, etc
        return obj


class JournalDetailView(View):
    template_name = "journal_detail.html"
    def get(self, request, id=None, *args, **kwargs):
        # initializes with a id=None incase no id is passed
        context={}
        if id is not None:
            obj = get_object_or_404(Journal, id= id)
            context['object'] = obj
        return render(request, self.template_name, context)

class JournalCreateView(View):
    template_name = "journal_create.html"
    def get(self, request, *args, **kwargs):
        # GET Requests
        form = JournalForm()
        context = {
            'form' : form
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        # POST Requests
        form = JournalForm(request.POST)
        if form.is_valid():
            form.save()
            form = JournalForm()
        context ={
                'form' : form
        }
        return render(request, self.template_name, context)

class JournalUpdateView(View):
    template_name = "journal_update.html"
    def get_object(self):
        id = self.kwargs.get('id') # gets the id passed into the url
        obj = None
        if id is not None:
            obj = get_object_or_404(Journal, id = id) # gets the objects with the given id
        return obj

    def get(self, request, id=None, *args, **kwargs):
        # GET Requests
        context = {}
        obj = self.get_object() # gets the object with given id
        if obj is not None:
            form = JournalForm(instance=obj) # initializes the form of the given object
            context['object'] = obj
            context['form']   = form
        return render(request, self.template_name, context)
    
    def post(self, request, id=None, *args, **kwargs):
        # POST Requests
        context = {}
        obj = self.get_object() # gets the object with given id
        if obj is not None:
            form = JournalForm(request.POST, instance=obj) # modifies the given objects form with POST data
            if form.is_valid():
                form.save() 
                return redirect('../') # redirects to object detail page
            context['object'] = obj
            context['form'] = form
            # if there is a validation error the page re-renders with given details
        return render(request, self.template_name, context)
    
class JournalDeleteView(GetObjectMixin, View):
    template_name = "journal_delete.html"
  
    def get(self, request, id=None, *args, **kwargs):
        # GET Requests
        context = {}
        obj = self.get_object() # inherits from GetObjectMixin
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)
    
    def post(self, request, id=None, *args, **kwargs):
        # POST Requests
        context = {}
        obj = self.get_object() 
        if obj is not None:
            obj.delete() # deletes the object on a post request
            return redirect('../../') # redirects to object list page
        return render(request, self.template_name, context)