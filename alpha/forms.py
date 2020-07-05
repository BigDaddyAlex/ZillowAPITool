from django import forms

class UploadFileForm(forms.Form):
    File = forms.FileField()
    File.widget.attrs.update({'class' : 'button'})