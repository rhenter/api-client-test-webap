from django.conf import settings
from django.utils.translation import activate

activate('en')


def pytest_configure():
    settings.LANGUAGE_CODE = 'en'
