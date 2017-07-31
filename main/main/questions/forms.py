from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Question, Answer
from main.equipments.models import Equipment, Area

class QuestionForm(forms.ModelForm):
    title = forms.CharField(
        max_length=255,
        label=_('Title'),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        max_length=2000,
        label=_('Description'),
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        help_text=' ',
    )
    tags = forms.CharField(
        max_length=255,
        required=False,
        label=_('Tags'),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text=_('Use spaces to separate the tags, \
                     such as "asp.net mvc5 javascript"')
    )

    source_area = forms.ModelChoiceField(widget=forms.Select(),
                                      queryset=Area.objects.all())
    destination_area = forms.ModelChoiceField(widget=forms.Select(),
                                      queryset=Area.objects.all())
    source_equipment = forms.ModelChoiceField(widget=forms.Select(),
                                      queryset=Equipment.objects.all())
    quantity = forms.IntegerField()
    

    class Meta:
        model = Question
        fields = ['title', 'description', 'tags']


class AnswerForm(forms.ModelForm):
    question = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                      queryset=Question.objects.all())
    description = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'})
    )

    class Meta:
        model = Answer
        fields = ['question', 'description']
