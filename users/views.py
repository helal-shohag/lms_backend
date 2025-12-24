from django.shortcuts import render
from .serializers import UserSrializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from .models import UserModel
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET','POST'])
def user_list(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return Response({'details':'Authentication credentials were not provided.'},status=status.HTTP_401_UNAUTHORIZED)
            
        if request.user.role == 'admin':
            user = UserModel.objects.all()
        else:
            user = UserModel.objects.filter(id = request.user.id)
            serializers = UserSrializer(user,many = True)   
            return Response(serializers.data) 