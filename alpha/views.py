from django.shortcuts import render,redirect
import csv
from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
from .Read import APIconnection
import pandas as pd
import os
from .forms import UploadFileForm
from django.contrib import messages 
from django.core.files.storage import FileSystemStorage,default_storage
from django.views.static import serve 
from django.http import HttpResponse, Http404

def homepage(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            inputfile=request.FILES['File']
            df = pd.read_csv(inputfile) 
            df.dropna()
            apiconnection=APIconnection(df)
            apiconnection.connect()
        else:
            messages.error(request, "Error")
            return render(request, 'index.html', {'form':form})
        return redirect('download/')
    else:
        form=UploadFileForm()
        return render(request,'index.html',{'form':form})

        
def downloadpage(request):
    currdir=os.path.join(os.getcwd(),'output.csv')
    with open(currdir, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(currdir)
        return response

    



