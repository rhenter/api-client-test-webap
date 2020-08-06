from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django_api_client.mixins import BaseViewMixin

from apps.core.clients import bookstore_client

User = get_user_model()


class HomeSiteView(BaseViewMixin, TemplateView):
    template_name = "home/home.html"
    page_title = 'Home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_books'] = bookstore_client.book.books.list().as_obj().count
        return context
