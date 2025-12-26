from django.http import HttpResponse

import os
from django.shortcuts import render
from requests import request

def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("<a href='https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7'> Django Playlist </a> <a href='/'> HomePage </a>")

# def RemovePunc(request):
#     #Get the Text
#     print(request.GET.get('text', 'default'))
#     #Analyze the Text
#     return HttpResponse("Remove Punc Django Playlist </a> <a href='/'> HomePage </a>")

def CapitalizeFirst(request):
    return HttpResponse("Capitalize First Django Playlist </a> <a href='/'> HomePage </a>")

def CapitalizeLater(request):
    return HttpResponse("Capitalize later This Django project <a href='/' HomePage </a>")

def SpaceRemover(request):
    return HttpResponse("Space Remover Django Playlist <a href='/'> HomePage </a>")

def LineRemover(request):
    return HttpResponse("New Line Remover Django Playlist <a href='/'> HomePage </a>")

def CharCount(request):
    return HttpResponse("Character Count Django Playlist <a href='/'> HomePage </a>")

def NewLineRemover(request):
    return HttpResponse("New Line Remover Django Playlist </a href='/'> HomePage </a>")

def analyze(request):
    djtext=request.GET.get('text','default')
    print(djtext)
    removepunc=request.GET.get('removepunc','off')
    print(removepunc)
    punctuations = ".,?!:;-_(){}[]'\".../\\@#$%&*+=<>^~`|"
    analyzed=djtext
    if removepunc=='on':
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuation','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    else:
        return HttpResponse("Error")
                
    
    # params={'purpose':'Removed Punctuation','analyzed_text':analyzed}
    # return render(request, 'analyze.html',params)









