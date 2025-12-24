from django.shortcuts import render
from rest_framework.response import Response
from .models import Category,Course
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Category
from .serializres import CategorySerializer


# Create your views here.
@api_view(['GET','POST'])
def categoryview(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializers =CategorySerializer(categories,many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        if request.user.role != 'admin':
            return Response({'error':'Only admin can create category'},status=403)
        else:
            serializers = CategorySerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data,status=201)
@api_view(['GET','POST'])
def courseview(request):
    if request.method == 'GET':
        if request.user.role in ['student','admin']:
            course = Course.objects.all()
        elif request.user.role == 'instructor':
            course = Course.objects.filter(instructor=request.user)
        else:
            return Response({'error':'Invalid role'},status=403)        