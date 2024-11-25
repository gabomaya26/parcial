from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import AuthorSerializer, MessageSerializer
from .models import Author, Message


@api_view(["GET"])
def get_messages(request):
    messages = Message.objects.all().order_by("created_at")
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_message(request):
    username = request.data.get("username")
    content = request.data.get("content")
    
    if not username or not content:
        return Response(
            {"error":"Los campos son requeridos."}, status=status.HTTP_400_BAD_REQUEST
        )
    
    author, _ = Author.objects.get_or_create(name=username)
    
    serializer = MessageSerializer(data={"content": content})
    
    if serializer.is_valid():
        serializer.save(author=author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)