from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import FileForm

# Create your views here.
def form(request):
    form = FileForm()
    return render(request, "form.html", {"form": form})

def score(request):
    if request.method == "POST":
        return HttpResponseRedirect("/wynik")
    return render(request, "score.html")


