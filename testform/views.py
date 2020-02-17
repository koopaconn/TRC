from django.shortcuts import render,render_to_response
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,ListView,FormView,DeleteView,DetailView
from django_tables2 import SingleTableView,SingleTableMixin
from testform.forms import form_testform
from testform.tables import table_testform
from testform.models import model_testform
from django.contrib import messages
from django_filters.views import FilterView
from django.contrib.auth.decorators import login_required
import django_filters
from django.contrib.auth.models import User

class view_blockFilter(django_filters.FilterSet):
    blockID = django_filters.CharFilter(lookup_expr='exact')
    shoulderWidthDec = django_filters.CharFilter(lookup_expr='gte')

    class Meta:
        model = model_testform
        fields = {'blockID','shoulderWidthDec'}

class view_testformTable(SingleTableMixin,FilterView):
    model = model_testform
    table_class = table_testform
    template_name = 'testformList.html'
    filterset_class = view_blockFilter

    def blocks(self):
        return model_testform.objects.all()

class view_testformTableDelete(SingleTableMixin,FilterView):
    model = model_testform
    table_class = table_testform
    template_name = 'testformListDelete.html'
    filterset_class = view_blockFilter

    def blocks(self):
        return model_testform.objects.all()

class view_testformDetail(DetailView):
    model = model_testform
    context_object_name = 'testform_details'
    template_name = "testformDetail.html"

class view_testform(CreateView):
    model = model_testform
    form_class = form_testform
    template_name = "testform.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        form.save()
        return super(view_testform, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        form = form_testform
        messages.add_message(self.request, messages.SUCCESS, 'New Block was submitted')
        return reverse("testform:view_testform")

class view_testformUpdate(UpdateView):
    model = model_testform
    form_class = form_testform
    template_name = "testformUpdate.html"
    # template_name_suffix = '_update_form'

    def form_valid(self, form):
        global subDel
        self.object = form.save(commit=False)
        self.object.editBy = self.request.user
        form.save()
        if self.request.POST.get("formsubmit"):
            subDel=1
        if self.request.POST.get("formdelete"):
            self.object.delete()
            subDel=2
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, *args, **kwargs):
        form = form_testform
        if subDel==2:
            messages.add_message(self.request, messages.WARNING, 'Block was Deleted')
        if subDel==1:
            messages.add_message(self.request, messages.INFO, 'Block was Updated')
        return reverse("testform:view_testform")


class view_testformDelete(DeleteView):
    model = model_testform
    form_class = form_testform
    # template_name = "testformDelete.html"
    # template_name_suffix = '_delete_form'

    def get_success_url(self, *args, **kwargs):
        form = form_testform
        messages.add_message(self.request, messages.WARNING, 'Block was Deleted')
        return reverse("testform:view_testform")
