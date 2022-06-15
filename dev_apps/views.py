from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

@login_required(login_url="login") # if the user not login, send the user to the login page.
def createProject(request):
    profile = request.user.profile # 1.took the current loggin user
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile # 2. associating with the project owner
            project.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "dev_apps/project_form.html", context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile #only the owner can update his project
    project = profile.project_set.get(id=pk) # getting all the projects of that specific user
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "dev_apps/project_form.html", context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk) # only the owner of the project can delete on his own project
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'dev_apps/delete_template.html', context)


