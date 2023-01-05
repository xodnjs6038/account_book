from myapp.models import AccountBook
from myapp.serializers import AccountBookCreatePatchSerializer, AccountBookListSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class AccountBookView(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        queryset = AccountBook.objects.filter(user=request.user.id, is_delete=request.GET.get('deleted', False))
        serializer = AccountBookListSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountBookCreatePatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'code': '1', 'message': 'success'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, book_id, format=None):
        account_book = get_object_or_404(AccountBook, id=book_id)
        serializer = AccountBookCreatePatchSerializer(data=request.data, instance=account_book)
        if serializer.is_valid():
            serializer.save()
            return Response({'code': '1', 'message': 'success'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PATCH'])
    def toggle_active(request, book_id, format=None):
        account_book = get_object_or_404(AccountBook, id=book_id)
        account_book.toggle_active()
        return Response(account_book.delete_message, status=status.HTTP_200_OK)