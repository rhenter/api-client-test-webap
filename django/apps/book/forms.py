from django import forms
from django.utils.translation import gettext_lazy as _
from django_api_client.forms import DynamicForm


class BookForm(DynamicForm):
    is_active = forms.BooleanField(required=False)
    description = forms.CharField(label=_('Description'), widget=forms.Textarea(attrs={'rows': 10, 'cols': 20}))

    class Meta:
        dynamic_fields = {
            'name': _('Name'),
            'description': _("Description"),
            'is_active': '',
        }
