from django.urls import path

from .views.account_book_views import AccountBookView
from .views.account_book_detail_views import AccountBookDetailView

app_name = 'myapp'


urlpatterns = [
    path('books', AccountBookView.as_view()),
    path('books/<int:book_id>', AccountBookView.as_view()),
    path('books/toggle_active/<int:book_id>', AccountBookView.toggle_active),
    path('books/detail/<int:book_id>', AccountBookDetailView.as_view(), name='book_details'),
    path('books/detail/<int:book_id>/<int:detail_id>', AccountBookDetailView.as_view(), name='book_details'),
    path('books/detail/<int:book_id>/<int:detail_id>', AccountBookDetailView.detail, name='book_detail'),
    path('books/detail/copy/<int:book_id>/<int:detail_id>', AccountBookDetailView.copy, name='book_details_copy'),
    path('books/detail/toggle_active/<int:book_id>/<int:detail_id>', AccountBookDetailView.toggle_active, name='book_details_deleted'),
]