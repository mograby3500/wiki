from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
import markdown
from . import util

class searchForm(forms.Form):
    q = forms.CharField()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": searchForm(),
    })

def entery(request, title):
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
        if query in util.list_entries():
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

