from django.forms import ModelForm
from .models import Screening

class ScreeningForm(ModelForm):
  class Meta:
    model = Screening
    fields = ['date', 'location']

