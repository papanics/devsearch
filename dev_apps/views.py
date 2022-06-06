from django.shortcuts import render
from dev_apps.models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'dev_apps/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    context = {'project': projectObj, 'tags': tags}
    return render(request, 'dev_apps/single-project.html', context)


def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, "dev_apps/project_form.html", context)