from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from dev_apps.models import Project


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET':'/api/projects'}, #method and route
        {'GET':'/api/projects/id'},
        {'POST':'/api/projects/id/vote'},

        {'POST':'/api/users/token'}, #this is how we gonna login the users
        {'POST':'/api/users/token/refresh'},
    ]


    return Response(routes)


@api_view(['GET'])
#@permission_classes([IsAuthenticated]) # Restriction  route --> only the authenticated user can view the projects
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)

    