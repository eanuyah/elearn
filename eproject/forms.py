from django import forms
from django.forms import ModelForm
from .models import Regtable
from .models import Stafftasks

# Create your views here.
		
class AlltaskForm(ModelForm):

	class Meta:
		model = Stafftasks
		fields = ['tasktitle', 'description', 'classname']
		
