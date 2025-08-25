from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  # only authenticated users allowed

    def get(self, request):
        return Response({"message": "Hello, you are authenticated!"})