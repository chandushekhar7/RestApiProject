from django.shortcuts import render
from django.http import HttpResponse
from .seri import StudentSeri
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from rest_framework import status

def home(request):
    return HttpResponse('Hello SHEKHAR')

@api_view(['GET','POST'])
def Restapi(request):
    if request.method == 'GET':
        slist = Student.objects.all()
        seri = StudentSeri(slist, many=True)
        return Response(seri.data)

    if request.method == 'POST':
        seri = StudentSeri(data= request.data)
        if seri.is_valid():
            seri.save()
        #return Response(seri.data)
        return Response(seri.data,status=status.HTTP_201_CREATED)
