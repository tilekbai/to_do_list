from django.shortcuts import render
from to_do_list.models import Problem

# Create your views here.

def index_view(request):
    problems = Problem.objects.all()
    return render(request, 'index.html', context={'problems': problems})

def problem_view(request):
    problem_id = request.GET.get('id')
    problems = Problem.objects.get(id = problem_id)
    return render(request, 'problem_view.html', context={'problems': problems})

def remove_problem_view(request):
    problem_id = request.GET.get('id')
    problems = Problem.objects.get(id = problem_id).delete()
    return render(request, 'remove_problem.html')
    

def add_problem_view(request):
    
    if request.method == "GET":
        return render(request, 'add_problem.html')
    elif request.method == "POST": 
        description = request.POST.get("description")
        detailed_description = request.POST.get("detailed_description")
        status = request.POST.get("status")
        dead_line = request.POST.get("dead_line")

        problems = Problem.objects.create(
            description=description,
            detailed_description=detailed_description,
            status=status,
            dead_line=dead_line
        )
        return render(request, 'problem_view.html', context={'problems':problems})