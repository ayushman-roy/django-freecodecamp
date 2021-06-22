from django.forms import ModelForm,ValidationError
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'author',
            'body'
        ]
    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if len(str(title)) < 8:
            raise ValidationError('Your title is too short!')
        return title 
    # title validation, title is invalid if smaller than 8 characters
