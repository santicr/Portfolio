from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'main/index.html')

def contact(req):
    return render(req, 'main/contact.html')

def about(req):
    return render(req, 'main/about.html')