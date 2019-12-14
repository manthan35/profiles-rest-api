from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test Api View"""
    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses Http method as a function(get,post,patch,push,delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'It mapped manually to URLs',
        ]
        return Response({'message':'Hello!!', 'an_apiview':an_apiview})