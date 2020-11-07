from django.shortcuts import render
from .serializer import ClienteSerializer
from rest_framework import views, status
from rest_framework.response import Response
from .models import Cliente

# Create your views here.
class ClienteView (views.APIView):
    # When the URL related has a request by get protocol, the following method get is executed
    def get(self, request, *args, **kwargs):
        # Query to database. It is like a SELECT *
        qs= Cliente.objects.all()
        # It is like a traslator, traslates the db info to JSON format
        serializer=ClienteSerializer(qs, many= True)
        return Response(serializer.data)