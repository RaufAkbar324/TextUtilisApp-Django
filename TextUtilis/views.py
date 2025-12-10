from django.http import HttpResponse

import os
from django.shortcuts import render

# def home(request):
#     # Get the full path of the file
#     current_dir = os.path.dirname(__file__)

#     # Create the full path to english.txt
#     file_path = os.path.join(current_dir, 'english.txt')
#     # return HttpResponse(file_path)

#     # Open the file and read its content
#     with open(file_path, 'r') as file:
#         content = file.read()  # Read all text from the file

#     # Return the content as an HTTP response
#     return HttpResponse(content, content_type="text/plain")




def home(request):
    params={'name':'John','place':'Mars'}
    return render(request, 'index.html',params)

def about(request):
    return HttpResponse("<a href='https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7'> Django Playlist </a> <a href='/'> HomePage </a>")

def RemovePunc(request):
    return HttpResponse("Remove Punc Django Playlist </a> <a href='/'> HomePage </a>")

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









