from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Child, Report, Babysitter
from .forms import ChildForm, ReportForm, BabysitterForm

#Create your views here.

def profiles(request):
    if request.method == 'GET':
        children = Child.objects.all()
        babysitters = Babysitter.objects.all()
        form = BabysitterForm()
        return render(request, 'profiles.html', context={'children':children, 'babysitters':babysitters, 'form':form})

    if request.method == 'POST':
        form = BabysitterForm(request.POST)
        if form.is_valid():
             if 'save' in request.POST:
                name = form.cleaned_data['name']
                age = form.cleaned_data['age']
                gender = form.cleaned_data['gender']
                Babysitter.objects.create(name=name, age= age, gender=gender)
        return HttpResponseRedirect(reverse('profiles'))

def createprofile(request):
    if request.method == 'GET':
        children = Child.objects.all()
        babysitters = Babysitter.objects.all()
        form = ChildForm()
        return render(request, 'createprofile.html', context={ 'children': children, 'form': form, 'babysitters':babysitters})
  
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
        reports = Report.objects.all()
        children = Child.objects.all()
        form = ReportForm()
        return render(request, 'reports.html', context={'reports':reports, 'form':form, 'children':children})
    
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

def edit(request, report_id):
    if request.method=='GET':
        report=Report.objects.get(pk=report_id)
        form=ReportForm(initial={'meal':report.meal,'nap':report.nap,'potty':report.potty})
        return render(request=request, template_name='edit.html', context={'form':form, 'id':report_id})
    if request.method=='POST':
        form=ReportForm(request.POST)
        if form.is_valid():
            if 'save' in request.POST:
                meal = form.cleaned_data['meal']
                potty = form.cleaned_data['potty']
                nap = form.cleaned_data['nap']
                child_id = form.cleaned_data['child']
                selected_child = Child.objects.get(pk=child_id)
                Report.objects.update(meal=meal, potty=potty, nap=nap, child=selected_child)
            elif "delete" in request.POST:
                Report.objects.filter(pk=report_id).delete()
            return HttpResponseRedirect(reverse('report'))

def editchild(request, child_id):
    if request.method =='GET':
        child=Child.objects.get(pk=child_id)
        babysitters = []
        for babysitter in child.babysitters.all():
            babysitters.append(babysitter.babysitter_id)
        form=ChildForm(initial={'name':child.name, 'age':child.age, 'gender':child.gender, 'babysitters':babysitters})
        return render(request=request, template_name='editchild.html', context={ 'form': form, 'id': child_id })

    if request.method =='POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            if 'save' in request.POST:
                name = form.cleaned_data['name']
                age = form.cleaned_data['age']
                gender = form.cleaned_data['gender']
                babysitters = form.cleaned_data['babysitters']
                child = Child.objects.filter(pk=child_id)
                child.update(name=name, age=age, gender=gender)
                child[0].babysitters.set(babysitters)
            elif 'delete' in request.POST:
                Child.objects.filter(pk=child_id).delete()
        return HttpResponseRedirect(reverse('profiles'))
            


