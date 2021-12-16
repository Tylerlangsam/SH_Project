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
                babysitters = form.cleaned_data['babysitters']
                child = Child.objects.filter()
                child.create(name=name, age=age)
                child[0].babysitters.set(babysitters)
            elif 'delete' in request.POST:
                Child.objects.delete()
        return HttpResponseRedirect(reverse('profiles'))
