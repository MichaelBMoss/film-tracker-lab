from django.forms import ModelForm
from .models import Director

class DirectorForm(ModelForm):
  class Meta:
    model = Director
    fields = ['date', 'meal']

