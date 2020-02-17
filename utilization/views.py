from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import FormView,UpdateView
from utilization.forms import form_utilization
from utilization.models import model_utilization,model_name,model_project
from django.db.models import Sum
import datetime

week = ''

# model_utilization = None

class view_utilization(FormView):
    model = model_utilization
    form_class = form_utilization
    template_name = "utilization.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.week = week

        inputName = int(self.request.POST.get('name'))
        inputProj = int(self.request.POST.get('project'))
        inputHours = float(self.request.POST.get('hours'))
        inputName = model_name.objects.filter(id=inputName).values('name')[0].get('name')
        inputProj = model_project.objects.filter(id=inputProj).values('projectDesc')[0].get('projectDesc')

        model_utilization.objects.filter(name=inputName,project=inputProj,week=week).delete()
        if inputHours==0:
            print ('0',inputName,inputProj,week)
            model_utilization.objects.filter(name=inputName,project=inputProj,week=week).delete()
        elif week!='':
            form.save()
        else: return HttpResponseRedirect(reverse('utilization:view_weekVarGet'))
        return super(view_utilization, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        form = form_utilization
        return reverse("utilization:view_utilization")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        totNameHrs = model_utilization.objects.filter(week=week).values('name').order_by('name').annotate(total_hours=Sum('hours'))
        totWeek = model_utilization.objects.filter(week=week).aggregate(Sum('hours'))
        totUtil = model_utilization.objects.exclude(project='PTO').filter(week=week).aggregate(Sum('hours'))
        context['week'] = week
        hrsNames = []
        hrsTot = []
        for values in totNameHrs:
            hrsNames.append(values.get('name',''))
            hrsTot.append(values.get('total_hours',0))
        try:
            totUtil = float(totUtil.get('hours__sum',0))
            totUtil = round(totUtil/(len(hrsNames)*40)*100)
        except: totUtil = 0
        context['hrsNames'] = hrsNames
        context['hrsTot'] = hrsTot
        context['totWeek'] = totWeek.get('hours__sum',0)
        context['totUtil'] = totUtil
        return context

    def utilList(self):
        return model_utilization.objects.order_by('name','project').filter(week=str(week))


def view_utilizationNames(request):
    namesModel = model_name.objects.order_by('name').values('name')
    if request.method == 'POST':
        if request.POST.get("delete"):
            delName = str(request.POST.get('delete'))
            delName = model_name.objects.filter(name=delName)
            delName.delete()
        elif request.POST.get("updateName"):
            currName = str(request.POST.get('currName'))
            updateName = str(request.POST.get('updateName'))
            model_name.objects.filter(name=currName).update(name=updateName)
        elif request.POST.get("new"):
            newName = str(request.POST.get('new'))
            nm = model_name(name=newName)
            nm.save()
        if week!='':
            return HttpResponseRedirect(reverse('utilization:view_utilization'))
        if week=='':
            return HttpResponseRedirect(reverse('utilization:view_weekVarGet'))
    return render(request,'utilizationNames.html',{'namesModel': namesModel})

def view_utilizationProjects(request):
    namesModel = model_project.objects.order_by('projectDesc').values('projectDesc')
    if request.method == 'POST':
        if request.POST.get("delete"):
            delName = str(request.POST.get('delete'))
            delName = model_project.objects.filter(projectDesc=delName)
            delName.delete()
        elif request.POST.get("updateName"):
            currName = str(request.POST.get('currName'))
            updateName = str(request.POST.get('updateName'))
            model_project.objects.filter(projectDesc=currName).update(projectDesc=updateName)
        elif request.POST.get("new"):
            newName = str(request.POST.get('new'))
            nm = model_project(projectDesc=newName)
            nm.save()
        if week!='':
            return HttpResponseRedirect(reverse('utilization:view_utilization'))
        if week=='':
            return HttpResponseRedirect(reverse('utilization:view_weekVarGet'))
    return render(request,'utilizationProjects.html',{'namesModel': namesModel})

def view_weekVarGet(request):
    global week
    utilModel = model_utilization.objects.order_by().values('week').distinct()
    today = datetime.datetime.today().date()
    if request.method == 'POST':
        if request.POST.get("currWeek"):
            week = today + datetime.timedelta(days=-today.weekday(), weeks=0)
        elif request.POST.get("nextWeek"):
            week = today + datetime.timedelta(days=-today.weekday(), weeks=1)
        else:
            week = datetime.datetime.strptime(request.POST.get('pastWeek'),r'%Y-%m-%d').date()
        return HttpResponseRedirect(reverse('utilization:view_utilization'))
    return render(request,'utilizationweek.html',{'utilModel': utilModel})
