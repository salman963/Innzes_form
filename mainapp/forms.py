from django import forms
from mainapp.models import *
class item_form(forms.ModelForm):
    class Meta:
        model = item_info
        fields = ['name','category','sub_category','price','image','Active_InActive']