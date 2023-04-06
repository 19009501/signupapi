from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response 
from .serializers import *
from .models import * 
from rest_framework import status
class SignupViewSet(viewsets.ViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    def create(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    def list(self, request, *args, **kwargs):
        print("list")
        #queryset = self.objects(self.get_queryset())
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
    def destroy(self,request,pk=None):
        try:
          user=self.queryset.get(pk=pk)
        except UserProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({"status":"user get deleted"})
# Create your views here.
