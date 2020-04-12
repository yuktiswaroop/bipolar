from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def book_detail(request, pk): 
    
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def userbookdetail(request):   
   
    if request.method == 'GET':
    	book = Book.objects.filter(reader=request.user)
    	serializer = BookSerializer(book, many=True)
    	return Response(serializer.data)  

@api_view(['DELETE'])
@permission_classes((IsAuthenticated, ))
def userbookdelete(request,id):
	#id=request.data.id
	book = Book.objects.get(reader=request.user, id=id)
	book.delete()
	return Response({"message":"ok"})


@api_view(['PUT'])
@permission_classes((IsAuthenticated, ))
def userbookupdate(request,id):
	book = Book.objects.get(reader=request.user, id=id)
	book.title = request.data.title
	book.amazon_url = request.data.amazon_url
	book.genre = request.data.genre
	book.author = request.data.author
	book.save()
	serializer = BookSerializer(book)
	return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def userbookcreate(request):
	params=request.data
	book=Book.objects.create(reader=request.user,title = params.title, amazon_url = params.amazon_url, genre=params.genre, author = params.author).save()
	serializer = BookSerializer(book, many=True)
	return Response(serializer.data)  

