from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea



class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Название заказа',
            }),
            'anons': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Краткое описание заказа',
            }),
            'full_text': Textarea(attrs={
                'class':'form-control',
                'placeholder':'Что было сделано?',
            }),
            'date': DateTimeInput(attrs={
                'class':'form-control',
                'placeholder':'Дата заказа',
            }),
        }