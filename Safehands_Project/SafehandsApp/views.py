from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Child, Report
from .forms import ChildForm, ReportForm

#Create your views here.

def profiles(request):
    #children is our queryset of Child objects
    children = Child.objects.all()
    return render (request, 'profiles.html', context={'children':children})

def createprofile(request):
    if request.method == 'GET':
        children = Child.objects.all()
        form = ChildForm()
        return render(request, 'createprofile.html', context={ 'children': children, 'form': form})
  
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            if 'save' in request.POST:
                name = form.cleaned_data['name']
                age = form.cleaned_data['age']
                gender = form.cleaned_data['gender']
                babysitters = form.cleaned_data['babysitters']
                child = Child.objects.filter()
                child.create(name=name, age=age, gender=gender)
                child[0].babysitters.set(babysitters)
        return HttpResponseRedirect(reverse('profiles'))

def report(request):
    if request.method == 'GET':
 # child = Child.objects.get(pk=child_id)
        reports = Report.objects.all()
        form = ReportForm()
        return render(request, 'reports.html', context={'reports':reports, 'form':form})
    
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            if 'save' in request.POST:
                meal = form.cleaned_data['meal']
                potty = form.cleaned_data['potty']
                nap = form.cleaned_data['nap']
                child_id = form.cleaned_data['child']
                selected_child = Child.objects.get(pk=child_id)
                Report.objects.create(meal=meal, potty=potty, nap=nap, child=selected_child)
            return HttpResponseRedirect(reverse('report'))


