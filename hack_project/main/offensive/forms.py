from django import forms 
from .models import PollOffensive

class PollForm(forms.ModelForm):
    class Meta:
        model = PollOffensive
        fields = '__all__'
        


        