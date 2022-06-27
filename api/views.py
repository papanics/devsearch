from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from dev_apps.models import Project, Review


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


#sending post request
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile # remember that the user is no longer in the session, it is in the token.
    data = request.data

    review, created = Review.objects.get_or_create( #if the user already has a review on that project then it will get or return that user else create a review.
        owner=user,
        project=project,
    )

    review.value = data['value']
    review.save()
    project.getVoteCount

    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)

    