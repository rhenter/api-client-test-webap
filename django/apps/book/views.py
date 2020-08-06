from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django_api_client.views import ClientAPICreateView, ClientAPIListView, ClientAPIUpdateView

from apps.core.clients import bookstore_client
from .forms import BookForm


class BookListView(ClientAPIListView):
    http_method_names = ['get']
    template_name = "book/book_list.html"
    page_title = _('Books List')
    client_method = bookstore_client.book.books.list
    paginate_by = 20


class BookCreateView(ClientAPICreateView):
    form_class = BookForm
    template_name = "book/book_form.html"
    success_url = reverse_lazy('book:list')
    page_title = _('New Book')
    client_method = bookstore_client.book.books.create


class BookUpdateView(ClientAPIUpdateView):
    form_class = BookForm
    template_name = "book/book_form.html"
    success_url = reverse_lazy('book:list')
    page_title = _('Edit Book')
    client_method = bookstore_client.book.books.update
    client_initial_method = bookstore_client.book.books.get
