from django.shortcuts import render

# Create your views here.
def tiktok(request):
    return render(request, 'tiktok/tiktok.html')


def details(request):
    pass