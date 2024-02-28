from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Review, Tag
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchProjects
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def projects(request):
    
    projects, search_query = searchProjects(request)

    # Set the paginator
    page = request.GET.get('page')
    results = 3
    paginator = Paginator(projects,results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    context = {'projects':projects, 'search_query':search_query, 'paginator':paginator}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project':projectObj})

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile

    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    # project = Project.objects.get(id=pk)
    project = profile.project_set.get(id=pk)

    form = ProjectForm(instance=project)

    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST,  request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method=='POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request, 'projects/delete_template.html', context)