from django.shortcuts import render
from .models import Movie, Guest, Reservation
from django.http.response import JsonResponse 
from rest_framework.decorators import api_view
from .serializers import GuestSerializer
from rest_framework.response import Response
from rest_framework import status, filters


# without rest framework
def no_framework(request):
    data = Guest.objects.all()
    response = {
        'guests': list(data.values('name', 'phone_number'))
    }

    return JsonResponse(response)

@api_view(['GET', 'POST'])
def FBV_list(request):
    # get
    if request.method =="GET":
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many = True)
        return Response(serializer.data)
    

    # post
    if request.method =="POST":
        serializer = GuestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def FBV_pk(request, id):
    try:
        guest = Guest.objects.get(id = id)
    except Guest.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    # get
    if request.method =="GET":
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    
    # put
    if request.method =="PUT":
        serializer = GuestSerializer(guest, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        
    # delete
    if request.method =="DELETE":
        guest.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



