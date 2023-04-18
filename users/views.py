from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomUserCreateView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token_serializer = CustomTokenObtainPairSerializer(data=request.data)
        token_serializer.is_valid(raise_exception=True)
        token = token_serializer.validated_data

        return Response({
            'user': serializer.data,
            'token': token,
        }, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

