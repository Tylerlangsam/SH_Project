from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Child, Report, Babysitter
from .forms import ChildForm, ReportForm, BabysitterForm

#Create your views here.

def profiles(request):
    if request.method == 'GET':
        # The children and babysitters are objects that have been retrieved from the database using queries
        children = Child.objects.all()
        babysitters = Babysitter.objects.all()
        #The code first creates an instance of the form class, which is then passed into the template as context.
        form = BabysitterForm()
        #The code is trying to render the profile page for a user.
        return render(request, 'profiles.html', context={'children':children, 'babysitters':babysitters, 'form':form})
        #The code starts by checking if the request method is POST.
    if request.method == 'POST':
        # a form called BabysitterForm() will be created with the data from the request.
        form = BabysitterForm(request.POST)
        #The code checks to see if there are any errors in the form and if so, it sends back an error message.
        if form.is_valid():
            #If there are no errors in the form, then it checks to see if 'save' was included in the POST data.
             if 'save' in request.POST:
                name = form.cleaned_data['name']
                age = form.cleaned_data['age']
                gender = form.cleaned_data['gender']
                # If so, then a new babysitter object will be created with all of that information and sent back as an HTTP response redirect to "profiles".
                Babysitter.objects.create(name=name, age= age, gender=gender)
                # The code is the code for a view function that will be called when the URL '/profiles/' is requested.
        return HttpResponseRedirect(reverse('profiles'))
                # The code is trying to create a profile page for the user
def createprofile(request):
    if request.method == 'GET':
        #The code first creates an instance of ChildForm and then renders it with the context of children, form, and babysitters.
        children = Child.objects.all()
        babysitters = Babysitter.objects.all()
        form = ChildForm()
        #The code will render the createprofile.html page with all of the child and babysitter data that is available in the database.
        return render(request, 'createprofile.html', context={ 'children': children, 'form': form, 'babysitters':babysitters})
  
    if request.method == 'POST':
        #The code starts by setting up a form with the POST data.
        form = ChildForm(request.POST)
        if form.is_valid():
            # It then checks to see if the user has saved their profile, and if so it sets the name, age, gender and babysitters of the child to whatever was in that field.
            if 'save' in request.POST:
                name = form.cleaned_data['name']
                age = form.cleaned_data['age']
                gender = form.cleaned_data['gender']
                babysitters = form.cleaned_data['babysitters']
                child = Child.objects.filter()
                child.create(name=name, age=age, gender=gender)
                child[0].babysitters.set(babysitters)
                #Finally, it redirects back to profiles after saving this new child.
        return HttpResponseRedirect(reverse('profiles'))

def report(request):
        #The code is trying to render a report form.
    if request.method == 'GET':
        #The code first gets all the reports and then it gets all the children of those reports.
        reports = Report.objects.all()
        children = Child.objects.all()
        form = ReportForm()
        #The code is using a function called render that takes in two parameters: request, which is an object representing the HTTP request, and context, which is an object containing information about what should be rendered on the page.
        return render(request, 'reports.html', context={'reports':reports, 'form':form, 'children':children})
    
    if request.method == "POST":
        #The code starts by creating a form with the POST data.
        form = ReportForm(request.POST)
        #The code then checks if the form is valid and, if so, it creates a new report for that meal, potty, nap and child.
        if form.is_valid():
            if 'save' in request.POST:
                meal = form.cleaned_data['meal']
                potty = form.cleaned_data['potty']
                nap = form.cleaned_data['nap']
                child_id = form.cleaned_data['child']
                selected_child = Child.objects.get(pk=child_id)
                Report.objects.create(meal=meal, potty=potty, nap=nap, child=selected_child)
                #It returns an HTTP response redirect to the user's original request URL.
            return HttpResponseRedirect(reverse('report'))

def edit(request, report_id):
        #The code starts by checking if the request is a GET.
    if request.method=='GET':
        #if it is, then the code gets the report with that ID and creates a form to edit that report
        report=Report.objects.get(pk=report_id)
        form=ReportForm(initial={'meal':report.meal,'nap':report.nap,'potty':report.potty})
        return render(request=request, template_name='edit.html', context={'form':form, 'id':report_id})
        #The code starts by checking if the request method is POST.
    if request.method=='POST':
        # If it is, then a form called ReportForm() will be created with the data from the POST request.
        form=ReportForm(request.POST)
        #The code checks to see if this form has been validated and if so, it checks to see if 'save' was in the POST data.
        if form.is_valid():
        #If 'save' was in the POST data, then a meal object will be created with potty, nap and child objects as attributes.
            if 'save' in request.POST:
        #Then these new objects are saved into an SQLite database table called Report using Python's built-in library for SQLite (sqlite3).
                meal = form.cleaned_data['meal']
                potty = form.cleaned_data['potty']
                nap = form.cleaned_data['nap']
                child_id = form.cleaned_data['child']
                selected_child = Child.objects.get(pk=child_id)
                Report.objects.update(meal=meal, potty=potty, nap=nap, child=selected_child)
        #If instead of saving a new report, delete was sent back from the server as part of a post request, then all records related to that report are deleted from the database table
            elif "delete" in request.POST:
                Report.objects.filter(pk=report_id).delete()
            return HttpResponseRedirect(reverse('report'))

def editchild(request, child_id):
    #The code starts by checking if the request is a GET.
    if request.method =='GET':
    #If it is, then it will get the child object and create a form with all of its attributes.
        child=Child.objects.get(pk=child_id)
        babysitters = []
        for babysitter in child.babysitters.all():
            babysitters.append(babysitter.babysitter_id)
        form=ChildForm(initial={'name':child.name, 'age':child.age, 'gender':child.gender, 'babysitters':babysitters})
        #The code returns this form to be rendered on the page.
        return render(request=request, template_name='editchild.html', context={ 'form': form, 'id': child_id })
        #The code starts by checking if the request method is POST.
    if request.method =='POST':
        # If it is, then a form object called ChildForm is created and assigned to the request.
        form = ChildForm(request.POST)
        if form.is_valid():
            if 'save' in request.POST:
        #The code checks if these values are not empty strings or None before assigning them to variables of type string.
                name = form.cleaned_data['name']
                age = form.cleaned_data['age']
                gender = form.cleaned_data['gender']
                babysitters = form.cleaned_data['babysitters']
                #The next line assigns an instance of class Child to the child_id parameter in the URL path for this page (i.e., profiles/<child_id>).
                child = Child.objects.filter(pk=child_id)
                child.update(name=name, age=age, gender=gender)
                child[0].babysitters.set(babysitters)
            elif 'delete' in request.POST:
                Child.objects.filter(pk=child_id).delete()
        return HttpResponseRedirect(reverse('profiles'))
            


