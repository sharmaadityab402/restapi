from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework import status
from django.http import Http404
from . serializers import *
# Create your views here.
class employeelist(APIView):
    def get(self,request):
        model=employee.objects.all()
        serializer=employeeSerializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = employeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class employeedetails(APIView):

    def get(self,request,employee_id):
        model=employee.objects.get(id=employee_id)
        serializer=employeeSerializer(model)
        return Response(serializer.data)

    def put(self,request,employee_id):
        serializer = employeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)






