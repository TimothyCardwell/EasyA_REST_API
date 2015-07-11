from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_api.serializers import *


# Create your views here.
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = Users.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return JSONResponse(user_serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JSONResponse(user_serializer.data, status=201)
        return JSONResponse(user_serializer.errors, status=400)


@csrf_exempt
def user_detail(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return JSONResponse(user_serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JSONResponse(user_serializer.data)
        return JSONResponse(user_serializer.errors, status=400)
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)