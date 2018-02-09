from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import userForm
from .models import fileupload
from .models import userDetails
import csv

def index(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)

def upload_csv(request):
    variables={}
    form_data={}
    if request.method == 'POST':
        form = userForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            names = []
            locations = []
            fileName = request.FILES['file'].name
            with open('media/documents/'+fileName) as csvDataFile:
                csvReader = csv.reader(csvDataFile)
                csvReader.next()
                                
                print fileName
                for row in csvReader:
                    names.append(row[0])
                    locations.append(row[1])
            userlist = dict(zip(names, locations))
            dictlength = len(userlist)
            for i in range(dictlength):
                form_data['name'] = names[i]
                form_data['location'] = locations[i]
                userDetails.objects.create(**form_data)
            return render(request,'forms/userview.html', {'userlist':userlist})

    else:
        form = userForm()
    return render(request, 'forms/userform.html', {'form': form })    