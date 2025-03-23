from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model
from .models import Book
from .serializers import AdminSignupSerializer, BookSerializer, AdminLoginSerializer

User = get_user_model()

class AdminSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AdminSignupSerializer
    permission_classes = [AllowAny]  # Allow anyone to register an admin

class AdminLoginView(generics.GenericAPIView):
    serializer_class = AdminLoginSerializer  # ✅ Fix: Add serializer_class

    permission_classes = [AllowAny]  # Allow anyone to access login

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(request, email=email, password=password)  # ✅ Fix: Use authenticate()

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }, status=status.HTTP_200_OK)

        return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class StudentView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
