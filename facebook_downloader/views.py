from django.shortcuts import render

# Create your views here.
def facebook(request):
    return render(request, 'facebook/facebook.html')


def details(request):
    pass