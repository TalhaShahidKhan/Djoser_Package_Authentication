from django.contrib.auth import get_user_model
from rest_framework.serializers import Serializer
User = get_user_model()


class CustomUserSerializer(Serializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')