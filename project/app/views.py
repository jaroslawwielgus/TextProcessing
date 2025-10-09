from django.shortcuts import render

# Create your views here.
def form(request):
    return render(request, "form.html")

def score(request):
    return render(request, "score.html")

