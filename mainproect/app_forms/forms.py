from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ArticlesForm(ModelForm):


    class Meta:
        model = Articles
        fields = ['tittle', 'anons', 'full_text', 'date']

        widgets = {

            "tittle": TextInput(attrs={
                'class': "form-control",
                "placeholder": "Название статьи"
            }),

            "anons": TextInput(attrs={
                'class': "form-control",
                "placeholder": "Анонс статьи"
            }),

            "date": DateTimeInput(attrs={
                'class': "form-control",
                "placeholder": "Дата публикации"

            }),

            "full_text": Textarea(attrs={
                'class': "form-control",
                "placeholder": "Текст статьи"
            }),


        }


