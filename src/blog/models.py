from django.db import models
from django.urls import reverse
# Create your models here.

class Article(models.Model):
    title   = models.CharField(max_length = 40)
    author  = models.CharField(max_length = 30)
    body    = models.TextField(blank=False, null= False)
    date    = models.DateField(null=True)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
        # redirects to the instance's detail page
        