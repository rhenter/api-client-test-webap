from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login/', auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True),
        name='login'),
    url(r'logout/', auth_views.logout_then_login, name='logout'),
]

application_urlpatterns = [
    url(r'', include('apps.core.urls', namespace='core')),
    url(r'^book/', include('apps.book.urls', namespace='book')),
]

urlpatterns.extend(application_urlpatterns)
