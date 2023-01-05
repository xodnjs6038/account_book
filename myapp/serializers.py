from rest_framework import serializers
from users.models import User

from .models import AccountBook, AccountDetail

# 리스트
class AccountBookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountBook
        fields = ['memo', 'budget', 'is_delete']


# 생성, 수정
class AccountBookCreatePatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountBook
        fields = ['user', 'memo', 'budget']
        
class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetail
        fields = '__all__'
        
class AccountDetailPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetail
        fields = ['price', 'description', 'account_book']