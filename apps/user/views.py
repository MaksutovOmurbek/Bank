from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.user.models import User
from apps.user.serializer import UserSerializer, UserRegisterSerializer

# Create your views here.
class UserAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        print(self.request.method == "POST")
        if self.request.method == "POST":
            return UserRegisterSerializer
        return UserSerializer
