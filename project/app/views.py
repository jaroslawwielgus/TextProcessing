from django.shortcuts import render
from .forms import FileForm
import re, random

# Create your views here.
def form(request):
    form = FileForm()
    return render(request, "form.html", {"form": form})

def score(request):
    if request.method == "POST":
        uploaded_file = request.FILES['file']
        text = ''

        for line in uploaded_file:
            text += line.decode()

        pattern = r"[a-żA-Ż-']+"

        def shuffler(match):
            word = match.group(0)  

            if len(word) > 3:
                word_center = word[1:-1]
                chars = list(word_center)
                random.shuffle(chars)
                return word[0] + "".join(chars) + word[-1]
            else:
                return word

        new_text = re.sub(pattern, shuffler, text)
        return render(request, "score.html", {"text": new_text})

    return render(request, "score.html")


