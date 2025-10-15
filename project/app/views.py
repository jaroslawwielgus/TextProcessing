from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import FileForm
from .models import ProcessedFile
import re, random

def form(request):
    file_form = FileForm()
    
    if request.method == "POST":
        file_form = FileForm(request.POST, request.FILES)
        
        if file_form.is_valid():
            uploaded_file = file_form.cleaned_data['file']
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
            processed_file = ProcessedFile(name="nazwa", processed_content=new_text)
            processed_file.save()
            return HttpResponseRedirect("/wynik/")
        
    return render(request, "form.html", {"form": file_form})

def score(request):
    file = ProcessedFile.objects.last()
    return render(request, "score.html", {"text": file.processed_content})




