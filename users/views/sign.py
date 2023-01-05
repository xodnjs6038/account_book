from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import (UserInfoSerializer, UserSignInSerializer, UserSignUpSerializer)

# Create your views here.
class UserSignUpView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserSignInView(APIView):
    
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.user_signin(data=request.data), status=status.HTTP_200_OK)


class UserSignOutView(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Refresh_token = request.data["refresh"]
        token = RefreshToken(Refresh_token)
        token.blacklist()

        return Response({"detail": "success, signout"}, status=status.HTTP_200_OK)