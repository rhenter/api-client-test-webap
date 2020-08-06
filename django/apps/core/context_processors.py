from django.conf import settings


def application_info(request):
    """
    Return the current application info
    """
    return {
        'app_version': settings.APP_VERSION,
        'developer_name': settings.DEVELOPER_NAME,
        'developer_website': settings.DEVELOPER_WEBSITE,
    }
