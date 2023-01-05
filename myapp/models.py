from django.db import models

# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class IsDelete:

    def toggle_active(self):
        self.is_delete = not self.is_delete
        self.save()
        message = '삭제' if self.is_delete else '복구'
        self.delete_message = {'success': f'{message} 완료'}

    class Meta:
        abstract = True
        
class AccountBook(TimeStamp, IsDelete):
    user = models.ForeignKey('users.User', related_name='account_books', verbose_name='유저', on_delete=models.CASCADE)
    memo = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=9, decimal_places=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'account_books'

    def __str__(self):
        return f'user: {self.user.email} / memo: {self.memo}'


# 가계부 상세내용
class AccountDetail(TimeStamp, IsDelete):
    account_book = models.ForeignKey('AccountBook', related_name='account_details', verbose_name='가계부', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=0)
    description = models.CharField(blank=True, null=True, max_length=255)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'account_detail'

    def __str__(self):
        return f'memo: {self.account_book.memo} / price: {self.price}'
