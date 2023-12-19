from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def analyze(request):
    text=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    removespace=request.GET.get('removespace','off')
    removenumber=request.GET.get('removenumber','off')
    lowercase=request.GET.get('lowercase','off')
    uppercase=request.GET.get('uppercase','off')
    newlineremover=request.GET.get('newlineremover','off')
    if removepunc == "on":
            punctuations = '''!()-[]{};:'"+\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in text:
                if char not in punctuations:
                    analyzed = analyzed + char
            text=analyzed
            
            
    elif(removenumber=='on'):
            analyzed=""
            numbers="0123456789"
            for char in text:
                  if char not in numbers:
                        analyzed=analyzed+char
            text=analyzed
            
            
    elif(lowercase=="on"):
            analyzed = ""
            for char in text:
                analyzed = analyzed + char.lower()
            text=analyzed
    elif(uppercase=="on"):
            analyzed = ""
            for char in text:
                analyzed = analyzed + char.upper()
            text=analyzed
    elif(removespace=="on"):
            analyzed = ""
            for index, char in enumerate(text):
                if not(text[index] == " " and text[index+1]==" "):
                    analyzed = analyzed + char
            text=analyzed

    elif (newlineremover == "on"):
            analyzed = ""
            for char in text:
                if char != "\n" and char!="\r":
                    analyzed = analyzed + char
                else:
                    print("no")
            text=analyzed    
    params = {'analyzed_text': text}
    return render(request, 'analyze.html', params)
        


