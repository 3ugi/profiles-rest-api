from rest_framework.views  import APIView
from rest_framework.response import Response


# 30. Create first APIView
class HelloApiView(APIView):
    """ Test API View. """

    def get(self, request, format=None):
        """ Returns a list of APIView features. """

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Give you the most control over you application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})


class AnotherApiView(APIView):

    def get(self, request, format=None):

        an_apiview = [
            "Ha Ha Ha"
        ]

        return Response({'message': 'Another', 'an_apiview': an_apiview})
