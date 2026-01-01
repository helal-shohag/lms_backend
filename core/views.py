from django.shortcuts import render
from rest_framework.response import Response
from .models import Category,Course
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions  import IsAuthenticated
from rest_framework import status
from .serializres import CategorySerializer,CourseSerializer


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
                return Response(serializers.data,status=status.HTTP_201_CREATED)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','POST'])
def courseview(request):
    if request.method == 'GET':
       if request.user.role in ['admin','student']:
          course = Course.objects.all()
       elif request.user.role == 'instructor':
           course =Course.objects.filter(instructor = request.user)   
           serializers =CategorySerializer(course,many= True) 
       else:    
           return Response(serializers.data)
    elif request.method == 'POST':
        if request.user.role != 'admin':
            return Response({'error': 'Only admin can create Course'},status=status.HTTP_403_FORBIDDEN)
        serializers = CourseSerializer(data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
            
            
   

            