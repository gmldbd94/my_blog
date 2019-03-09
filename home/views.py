from django.shortcuts import render

#rest_framework를 위한 api
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
# Create your views here.
def index(request):
    return render(request, "index.html")

def project(request):
    pass

def about(APIView):
    pass

def blog(APIView):
    pass

def eductaion(APIView):
    pass

def project(APIView):
    pass

def study(APIView):
    pass

def qna(APIView):
    pass