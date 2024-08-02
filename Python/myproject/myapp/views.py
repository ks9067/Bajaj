from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserInputSerializer

class UserInfoView(APIView):

    def get(self, request):
        # For GET request, just return an operation code
        return Response({'operation_code': 'OP123'}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserInputSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                'status': 'success',
                'user_id': serializer.validated_data['user_id'],
                'college_email': serializer.validated_data['college_email'],
                'college_roll_number': serializer.validated_data['college_roll_number'],
                'numbers': serializer.validated_data['numbers'],
                'alphabets': serializer.validated_data['alphabets'],
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
