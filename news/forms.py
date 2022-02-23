from django import forms
import re
from django.core.exceptions import ValidationError

from .models import Category, News


# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=128, label='Название', widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#         }
#     ))
#     content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(
#         attrs={
#             'class': 'form-control',
#             'rows': 4,
#         }
#     ))
#     is_published = forms.BooleanField(label='Опубликовать', initial=True, required=False)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
#                                       empty_label='не выбрано', widget=forms.Select(
#             attrs={
#                 'class': 'form-control',
#             }
#         ))


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = (
            'title', 'content', 'photo', 'is_published', 'category',
        )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с числа или цифры!')
        return title
