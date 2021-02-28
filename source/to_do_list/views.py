from django.shortcuts import render
from to_do_list.models import Problem

# Create your views here.

def index_view(request):
    problems = Problem.objects.all()
    return render(request, 'index.html', context={'problems': problems})