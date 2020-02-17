from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class view_index(TemplateView):
    template_name = "index.html"

class view_test(TemplateView):
    template_name = "test.html"
