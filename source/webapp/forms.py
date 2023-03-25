from django import forms
from webapp.models import Product
from webapp.models import Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'image')
        labels = {
            'name': 'Название',
            'category': 'Категория',
            'description': 'Описание',
            'image': 'Картинка'
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('description', 'grade')
        labels = {
            'description': 'Текст отзыва',
            'grade': 'Оценка'
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')