
from django.shortcuts import render 
from rest_framework.response import Response
from rest_framework import viewsets
from api.models import  Employee , CustomUser
from rest_framework.viewsets import ModelViewSet
from api.serializers import  EmployeeSerializer , UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .custompremissions import IsEmployee , IsAdmin , IsManager
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny 
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.



# Employee Data With Role based 
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [JWTAuthentication]
    def get_permissions(self):
        if self.request.user.role == 'Admin':
            return [IsAdmin()]
        elif self.request.user.role == 'Manager':
            return [IsManager()]
        elif self.request.user.role == 'Employee':
            return [IsEmployee()]
        else:
            return []


# Register
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


register_user.permission_classes = [AllowAny]
    

#Login
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            return Response({'access_token': access_token, 'refresh_token': refresh_token}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


user_login.authentication_classes = [JWTAuthentication]



