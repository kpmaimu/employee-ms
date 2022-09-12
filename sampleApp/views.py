from django.shortcuts import render
from .models import Employee
# from .models import Employee,Image
# from .serializers import EmployeeSerializer,ImageSerializer
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class EmployeeList(APIView):
    def get(self,request,format=None):
        employees=Employee.objects.all()
        serializer=EmployeeSerializer(employees,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
       serializer=EmployeeSerializer(data=request.data)
       if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
       Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ImageUpload(APIView):

#     def post(self,request):
#         serializer=ImageSerializer(data=request.data)
#         print(request.data)
#         if(serializer.is_valid()):
#             serializer.save()
#             return Response("Successfully saved")
#         return Response("error")
    
#     def get(self,request):
#         images=Image.objects.all()
#         # serializer=ImageSerializer(images, many=True)
#         # print(serializer.data)
#         return Response(serializer.data)



      