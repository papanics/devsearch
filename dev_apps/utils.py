from django.db.models import Q
from .models import Project, Tag



def searchProjects(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter( #used disctinct() to not duplicate the items here.
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags) #many to many relationship with the projects

    )
    return projects, search_query