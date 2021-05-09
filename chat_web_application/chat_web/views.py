from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.
from chat_web.chat_start import *
def index(request):
    return render(request,"index.html",{'res':"chatzone"})
def click(request):
    sentence=request.POST.get("name")
    if(sentence==None):
        return render(request,"index.html",{'res':"chatzone"})
    res=start(sentence)
    print(res)
    print(str(sentence))

    sens=str(sentence).split(" ")


    return render(request,"index.html",{'input':sens,'res':res})