from django.forms import ModelForm, CharField

from words.models import Word


class WordForm(ModelForm):
    freeTrans2 = CharField(required=False)
    comment = CharField(required=False)

    class Meta:
        model = Word
        fields = ['word', 'freeTrans']
