from rest_framework.generics import CreateAPIView

from accounts.api.serializers import RegisterSerializer
# Create your views here.

class RegisterView(CreateAPIView):
    serializer_class  = RegisterSerializer

class LoginView():
    pass