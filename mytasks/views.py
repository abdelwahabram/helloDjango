from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

class NewTask(forms.Form):
    task = forms.CharField(label="Add New Task: ")
    # correctness = forms.BooleanField(label="Are you sure??",required=True)

# Create your views here.

def index(request):
    if "task" not in request.session:
        request.session["task"] = []
    return render(request,'mytasks/index.html',{
        "tasks":request.session["task"]
    })

def add(request):
    print(request.session["task"])
    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            if task not in request.session["task"]:
                request.session["task"] += [task]
                # request.session["task"].append(task)
                # print(request.session["task"])
                # https://stackoverflow.com/questions/63449525/append-to-request-sessionslist-in-django
                return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,'mytasks/add.html',{"form":form})
    return render(request,'mytasks/add.html',{"form":NewTask()})