from django.shortcuts import render
import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entery(request, title):
    f = util.get_entry(title)
    if f == None:
        entery_html = "<h1>Not Found</h1>"
    else:
        entery_html = markdown.markdown(f)
    
    return render(request, "encyclopedia/entery.html", {
        "title" : title,
        "entery" : entery_html
    })

