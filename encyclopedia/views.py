from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
import markdown
import random
from . import util

class searchForm(forms.Form):
    q = forms.CharField()


class EditForm(forms.Form):
    title = forms.CharField()

class NewEntryForm(forms.Form):
    title = forms.CharField(label= "Title", widget= forms.TextInput(attrs={
        'class' : 'form-control',
        'style' : 'width: 200px',
    }))
    md_content = forms.CharField( label="Markdown Content", widget= forms.Textarea(attrs={
        'class':'form-control',
        'style':'width: 800px; margin-bottom:20px;',
    }))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": searchForm(),
    })

def entery(request, title):
    if request.method == "GET":
        f = util.get_entry(title)
        if f == None:
            entery_html = "<h1>Not Found</h1>"
        else:
            entery_html = markdown.markdown(f)
        
        return render(request, "encyclopedia/entery.html", {
            "title" : title,
            "entery" : entery_html,
            "form": searchForm(),
        })
    


def search_results(request):
    form = searchForm(request.POST)
    query = ""
    
    if form.is_valid():
        query += form.cleaned_data["q"]
        query.replace(" ", "_")

        for q in util.list_entries():
            if query.lower() == q.lower():
                url = reverse("entery", kwargs = {"title" : query})
                return HttpResponseRedirect(url)
        else:
            matched_entries = []
            for entry in util.list_entries():
                qq = query.lower()
                en = entry.lower()

                if qq in en:
                    matched_entries.append(entry)

            return render(request, "encyclopedia/search_results.html", {
                "entries": matched_entries,
            })

def new_entry(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_entry.html", {
            "form" : NewEntryForm()
        })
    else:    
        if request.POST['action'] == "save":
            form = NewEntryForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data["title"]
                md_content = form.cleaned_data["md_content"]
                util.save_entry(title, md_content)
                url = reverse("entery", kwargs = {"title" : title})
                return HttpResponseRedirect(url)


        elif request.POST['action'] == "submit":
            #populate the form
            form = NewEntryForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data["title"]
                md_content = form.cleaned_data["md_content"]
                for entry in util.list_entries():
                    if title.lower() == entry.lower():
                        return render(request, "encyclopedia/new_entry.html", {
                            "form" : form,
                            "error" : f"This title already exists"
                        })

                #we should save this file to desk now
                title = title.replace(" ", "_")
                util.save_entry(title, md_content)
                #redirect the user to the entry page
                url = reverse("entery", kwargs = {"title" : title})
                return HttpResponseRedirect(url)
            else:
                return render(request, "encyclopedia/new_entry.html", {
                    "form" : form
                })

def edit_entry(request):
    if request.method == "POST":
        edit_form = EditForm(request.POST)
        if edit_form.is_valid():
            title= edit_form.cleaned_data["title"]
            return render(request, "encyclopedia/edit_entry.html", {
                "title" : title,
                "md_content" : util.get_entry(title),
            })


def random_entry(request):
    random_title = random.choice(util.list_entries())
    url = reverse("entery", kwargs = {"title" : random_title})
    return HttpResponseRedirect(url)