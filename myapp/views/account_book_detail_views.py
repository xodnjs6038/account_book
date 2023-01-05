from myapp.models import AccountBook, AccountDetail
from myapp.serializers import AccountDetailPostSerializer, AccountDetailSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class AccountBookDetailView(APIView):

    serializer_class = AccountDetailSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, book_id):
        account_book = get_object_or_404(AccountBook, id=book_id, user=request.user.id)
        account_details = account_book.account_details.filter(is_delete=request.GET.get('deleted', False))
        serializer = AccountDetailSerializer(account_details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, book_id):
        serializer = AccountDetailPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, book_id, detail_id):
        account_book = get_object_or_404(AccountBook, id=book_id, user=request.user.id)  # 가계부
        account_detail = get_object_or_404(AccountDetail, account_book=account_book.id, id=detail_id)  # 가계부 내역
        serializer = AccountDetailPostSerializer(account_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def detail(request, book_id, detail_id):
        account_book = get_object_or_404(AccountBook, id=book_id, user=request.user.id)  # 가계부
        account_detail = get_object_or_404(AccountDetail, account_book=account_book.id, id=detail_id)  # 가계부 내역
        serializer = AccountDetailSerializer(account_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @api_view(['PATCH'])
    def toggle_active(request, book_id, detail_id):
        account_book = get_object_or_404(AccountBook, id=book_id, user=request.user.id)  # 가계부
        account_detail = get_object_or_404(AccountDetail, account_book=account_book.id, id=detail_id)  # 가계부 내역
        account_detail.toggle_active()
        return Response(account_detail.delete_message, status=status.HTTP_200_OK)
    
    @api_view(['POST'])
    def copy(request, book_id, detail_id):
        account_detail_copy = AccountDetail.objects.get(id=detail_id)
        copy_data = account_detail_copy.__dict__
        copy_data['account_book'] = book_id
        serializer = AccountDetailPostSerializer(data=copy_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)