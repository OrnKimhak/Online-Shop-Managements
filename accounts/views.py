from rest_framework.generics import CreateAPIView
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.models import User
from accounts.api.serializers import RegisterSerializer
# Create your views here.

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class  = RegisterSerializer

# Protected Test View (Example)
class ProtectedProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({
            "message" : f"Hello{request.user.username}, you are authenticated",
            "user_id" : request.user.id,
            "email" : request.user.email,
        }, status=status.HTTP_200_OK)