# from django.shortcuts import render
#from django.template import loader
from . models import User



# ====  DRF  ====
from rest_framework import generics
from . import serializers
# def registration(request):
#     return render(request, 'registration.html')


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.User
    