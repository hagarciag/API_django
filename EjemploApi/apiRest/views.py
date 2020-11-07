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

    def post(self, request, *args, **kwargs):
            #Capturamos los valores de entrada
            try:
                num_doc=request.data['num_doc']
                tipo_num_doc=request.data['tipo_num_doc']
            except:
                # Error code 400 is returned because the request had a problem. Error codes: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
                return Response({},status= status.HTTP_400_BAD_REQUEST)
            # filter is like a WHERE of the SQL. If many records are returned, only one es taken ([:1])
            qs=Cliente.objects.filter(num_doc=num_doc, tipo_num_doc=tipo_num_doc)[:1]
            if len(qs)!=0:
                serializer=ClienteSerializer(qs, many=True)
                return Response(serializer.data)
            # Error code 204 is returned because it is the code for non-content returned. Error codes: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
            return  Response({},status= status.HTTP_204_NO_CONTENT)

# It is necessary to create a new VIEW because we are going to create a new POST method and only method type can be configured by VIEW.
class CreateView (views.APIView):

    def post(self, request, *args, **kwargs):
        data= request.data
        serializer= ClienteSerializer(data=data)
        # The information received in the body is the expected?
        if serializer.is_valid():
            # The client is INSERTED in the database
            serializer.save()
            # The same information received of the client is return and the status
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)