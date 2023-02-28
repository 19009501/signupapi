from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response 
from .serializers import *
from .models import * 
class SignupViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    def list(self,request):
        queryset=UserProfile.objects.all()
        serializer=UserProfileSerializer(queryset,many=True)
        return Response(serializer.data)
    def destroy(self,request,pk=None):
        user=self.get_object()
        serializer=UserProfileSerializer(user)
        serializer.delete()
        return Response({"status":"user get deleted"})
# Create your views here.
