from django import forms
from utilization.models import model_utilization,model_name,model_project

# model_utilization = None

class form_utilization(forms.ModelForm):

    name = forms.ModelChoiceField(queryset=model_name.objects.order_by('name').all(), empty_label=None, widget = forms.Select)
    project = forms.ModelChoiceField(queryset=model_project.objects.order_by('projectDesc').all(), empty_label=None)
    hours = forms.FloatField(error_messages={'invalid':"Please enter hours or 0 to delete entry",'required':"Please enter hours or 0 to delete entry"})
    week = forms.CharField(widget = forms.HiddenInput(),required=False)

    class Meta:
        model = model_utilization
        fields = '__all__'
