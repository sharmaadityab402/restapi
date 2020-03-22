from rest_framework.views import APIView
from rest_framework.response import Response
from  rest_framework import status
from  .serializers import *
from django.http import Http404
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
     def get_object(self,Employee_code):
         try:
             return employee.objects.get(pk=pk)
         except employee.DoesNotExist:
             raise Http404


         
    def get(self, request, Employee_id):
        try:
            model = employee.objects.get(id=employee_id)
        except employee.DoesNotExist:
            return Response(f'user with {id} is not found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = employeeSerializer(model)
        return Response(serializer.data)

    
    def put(self,request,employee_id):
        model = employee.objects.get(id=employee_id)
        serializer = employeeSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


