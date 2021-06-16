from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

from rest_framework.views import APIView

from rest_framework.authtoken.models import Token


# Create your views here.


class RegisterUserView(APIView):


    def post(self, request):
        serializers = UserSerializer(data = request.data)

        if not serializers.is_valid():
            return Response({'status': 403, "message": serializers.errors})

        else:
            serializers.save()

            # Token
            user = User.objects.get(username=serializers.data['username'])
            token , _ = Token.objects.get_or_create(user = user)
            return Response({'data': serializers.data, 'status': 200 ,'token' : str(token)})


# API for Student CRUD

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentAPI(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        students = Student.objects.all()
        print(students)
        serializers = StudentSerializer(students, many=True)
        print(serializers.data)
        print(request.user)
        return Response(serializers.data)


    def post(self, request):
        print(request.data)

        serializers = StudentSerializer(data=request.data)

        if not serializers.is_valid():
            return Response({'status': 403, "message": serializers.errors})

        else:
            serializers.save()
            return Response({'data': request.data, 'status': 200})



    def put(self, request):
        try:
            print(id)
            student = Student.objects.get(id=request.data['id'])

            serializers = StudentSerializer(student, data=request.data, partial=True)

            if not serializers.is_valid():
                return Response({'status': 403, "message": serializers.errors})

            else:
                serializers.save()
                return Response({'data': request.data, 'status': 200})
        except:
            return Response({'status' : 403 , 'message' : serializers.errors})

    def patch(self, request):
        try:
            print(id)
            student = Student.objects.get(id=request.data['id'])

            serializers = StudentSerializer(student, data=request.data, partial=True)

            if not serializers.is_valid():
                return Response({'status': 403, "message": serializers.errors})

            else:
                serializers.save()
                return Response({'data': request.data, 'status': 200})
        except:
            return Response({'status' : 403 , 'message' : serializers.errors})



    def delete(self, request):
        try:
            student = Student.objects.get(id=request.data['id'])
            student.delete()
            return Response({'status' : 200 , "message" : 'Successfully deleted'})
        except:
            return Response({'status' : 403 , 'message' : "Invalid ID"})




# @api_view(['GET'])
# def get(request):

#     students = Student.objects.all()
#     print(students)
#     serializers = StudentSerializer(students, many=True)
#     print(serializers.data)
#     return Response(serializers.data)


# # Get all Books
# @api_view(['GET'])
# def getBooks(request):

#     books = Book.objects.all()
#     serializers = BookSerializer(books, many=True)
#     print(serializers.data)
#     return Response(serializers.data)


# @api_view(['POST'])
# def post(request):
#     print(request.data)

#     serializers = StudentSerializer(data=request.data)

#     if not serializers.is_valid():
#         return Response({'status': 403, "message": serializers.errors})

#     else:
#         serializers.save()
#         return Response({'data': request.data, 'status': 200})


# @api_view(['PUT'])
# def update(request, id):
#     try:
#         print(id)
#         student = Student.objects.get(id=id)

#         serializers = StudentSerializer(student, data=request.data, partial=True)

#         if not serializers.is_valid():
#             return Response({'status': 403, "message": serializers.errors})

#         else:
#             serializers.save()
#             return Response({'data': request.data, 'status': 200})
#     except:
#         return Response({'status' : 403 , 'message' : serializers.errors})



# @api_view(['PATCH'])
# def update(request, id):
#     try:
#         print(id)
#         student = Student.objects.get(id=id)

#         serializers = StudentSerializer(student, data=request.data, partial=True)

#         if not serializers.is_valid():
#             return Response({'status': 403, "message": serializers.errors})

#         else:
#             serializers.save()
#             return Response({'data': request.data, 'status': 200})
#     except:
#         return Response({'status' : 403 , 'message' : serializers.errors})


# @api_view(['DELETE'])
# def delete(request, id):
#     try:
#         student = Student.objects.get(id=id)
#         student.delete()
#         return Response({'status' : 200 , "message" : 'Successfully deleted'})
#     except:
#         return Response({'status' : 403 , 'message' : "Invalid ID"})

