from django.shortcuts import render
from rest_framework.response import Response # type: ignore
from rest_framework.permissions import IsAuthenticated # type: ignore
from rest_framework.decorators import api_view, permission_classes # type: ignore

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secure_view(request):
    return Response({'message': 'This is a protected view.'})
