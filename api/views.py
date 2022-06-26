from django.http import JsonResponse

def getRoutes(request):

    routes = [
        {'GET':'/api/projects'}, #method and route
        {'GET':'/api/projects/id'},
        {'POST':'/api/projects/id/vote'},

        {'POST':'/api/users/token'}, #this is how we gonna login the users
        {'POST':'/api/users/token/refresh'},
    ]


    return JsonResponse(routes, safe=False) #safe=False --> return back something more than just a Python dictionary or turn any kind of data that we want into JSON data.
    