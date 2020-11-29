from rest_framework.views  import APIView
from rest_framework.response import Response
# 34. Add POST method to APIView
from rest_framework import status
# 39. Create a simple Viewset
from rest_framework import viewsets
# 51. Add authentication and permissions to Viewset
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
# 47. Create profiles ViewSet
from profiles_api import models
# 51. Add authentication and permissions to Viewset
from profiles_api import permissions

# 30. Create first APIView
class HelloApiView(APIView):
    """ Test API View. """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView features. """

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Give you the most control over you application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ Create a hello message with our name. """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

# 36. Add PUT, PATCH, and DELETE methods
    def put(self, request, pk=None):
        """ Handle updating an object. """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Handle a partial update of an object. """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Delete an object. """
        return Response({'method': 'DELETE'})


class AnotherApiView(APIView):

    def get(self, request, format=None):

        an_apiview = [
            "Ha Ha Ha"
        ]

        return Response({'message': 'Another', 'an_apiview': an_apiview})


# 39. Create a simple Viewset
class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet. """
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return a hello message. """

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """ Create a new hello message. """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ Handle getting an object by its ID. """
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ Handle updating and object. """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ Handle updating part of an object. """
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """ Handle removing an object. """
        return Response({'http_method': 'DELETE'})


# 47. Create profiles ViewSet
class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles. """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # 51. Add authentication and permissions to Viewset
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

