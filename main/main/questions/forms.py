from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Question, Answer
from main.equipments.models import Equipment, Area, EquipmentArea

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
                     such as "pc tv"')
    )
    source_area = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                      queryset=Area.objects.all(),label='原区域')
    destination_area = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                      queryset=Area.objects.all(),label='目标区域')
    source_equipmentarea = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                      queryset=EquipmentArea.objects.all(),label='设备')
    quantity = forms.IntegerField(label='数量')

    class Meta:
        model = Question
        fields = ['title', 'description', 'tags']

    def clean(self):
        cleaned_data = super(QuestionForm, self).clean()
        source_equipment = cleaned_data.get("source_equipmentarea")
        quantity = cleaned_data.get("quantity")

        if source_equipment.quantity < quantity:
            msg = "选择的设备数量超出范围."
            self.add_error('quantity', msg)
            raise forms.ValidationError("选择的设备数量超出范围")
        return cleaned_data 


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
