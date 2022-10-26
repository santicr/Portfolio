from django.shortcuts import render
from portfolio.models import Project

# Create your views here.
def portfolio(req):
    projects = Project.objects.all()
    return render(req, 'portfolio/portfolio.html', {'projects': projects})