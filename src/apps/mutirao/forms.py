from django import forms
from .models import Review

TRUE_FALSE_CHOICES = (
    (True, 'Sim'),
    (False, 'Não')
)

class MutiraoForm(forms.ModelForm):
    apoiar = forms.ChoiceField(choices=TRUE_FALSE_CHOICES, label="Devemos apoiar essa emenda?", 
        initial=False, widget=forms.Select(), required=True)
    justificativa = forms.CharField(required=False, widget=forms.Textarea)
    emenda_id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    
    class Meta:
        model = Review
        fields = ['apoiar', 'justificativa', 'emenda_id']
     