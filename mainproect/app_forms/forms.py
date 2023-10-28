from .models import Articles
from django.forms import ModelForm


class ArticlesForm(ModelForm):


    class Meta:
        model = Articles
        fields = ['tittle', 'anons', 'full_text', 'date']
