from rest_framework.views import APIView
from rest_framework.response import Response

class RegisterAPIView(APIView):
    def post(self, request):
        # Handle registration logic
        return Response({"message": "Registered successfully"})
