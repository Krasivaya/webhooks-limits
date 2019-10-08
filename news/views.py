from django.http import HttpResponse

# News View
def welcome(request):
    return HttpResponse('Welcome To The Moringa Tribune')
