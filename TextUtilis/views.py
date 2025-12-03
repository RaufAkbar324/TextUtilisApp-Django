from django.http import HttpResponse

import os

def home(request):
    # Get the full path of the file
    current_dir = os.path.dirname(__file__)

    # Create the full path to english.txt
    file_path = os.path.join(current_dir, 'english.txt')
    # return HttpResponse(file_path)

    # Open the file and read its content
    with open(file_path, 'r') as file:
        content = file.read()  # Read all text from the file

    # Return the content as an HTTP response
    return HttpResponse(content, content_type="text/plain")



def about(request):
    return HttpResponse("<a href='https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7'> Django Playlist </a>")