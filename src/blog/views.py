from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView
)
from .models import Article
from .forms import ArticleForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
# Create your views here.


class ArticleListView(ListView):
    queryset = Article.objects.all() # limits choices if used with filter, etc
    template_name = 'article_list.html'
    # overrides the default template location
    # looks for template by default at = <appname>/<modelname>_<genericclassname>.html
    # in this case blog/article_list.html

class ArticleCreateView(CreateView):
    template_name = 'article_create.html'
    queryset = Article.objects.all()
    form_class = ArticleForm # the form which is to be rendered out
    def form_valid(self, form):
        print(form.cleaned_data) # prints the form data in console
        return super().form_valid(form) # checks if form is valid via the built in validator
        # for demonstration purposes only since the above function didnt override anything

class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    def get_object(self):
        id_ = self.kwargs.get("id") 
        return get_object_or_404(Article, id = id_)
        # selects the object whoose id is passed into the url or returns a 404
        # queryset not needed as we need a single object, not a set

class ArticleUpdateView(UpdateView):
    template_name = 'article_update.html'
    form_class = ArticleForm
    queryset = Article.objects.all()
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id = id_)
    # initializes the form with the given object and updates it with modified data upon submission

class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id = id_)
        # returns the object which is to be deleted
    def get_success_url(self):
        return reverse("articles:article-list")
        # redirects to this page incase of deletetion since get_absolute_url will be an error
        # if any error in redirect, no object is deleted
