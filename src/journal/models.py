from django.db import models
from django.urls import reverse
# Create your models here.

class Journal(models.Model):
    title   = models.CharField(max_length=30)
    body    = models.TextField()
    date    = models.DateField(null=True)
    def get_absolute_url(self):
        return reverse("journal:Journal-detail", kwargs={"id": self.id})
