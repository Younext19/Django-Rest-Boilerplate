from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from connect.models import User
from connect.serializers import GetUserInfoSerializer, PostUserSerializer

# Create your views here.


class UserInfo(APIView):

    def get(self, request):
        users = User.objects.get(id=request.user.id)
        serializer = GetUserInfoSerializer(users)
        return Response(serializer.data)


class SignUp(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = PostUserSerializer(
            data=request.data, context={"request": request})

        if serializer.is_valid():
            serializer = serializer.save()
            serializer = GetUserInfoSerializer(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
