from django import forms
from django.core.validators import FileExtensionValidator

class FileForm(forms.Form):
    file = forms.FileField(validators=[FileExtensionValidator(['txt', 'html', 'css', 'xml'])], error_messages={"invalid_extension" : "Błąd! Akceptowane rozszerzenia pliku to: .txt, .html, .css oraz .xml", "empty": "Błąd! Plik jest pusty"})