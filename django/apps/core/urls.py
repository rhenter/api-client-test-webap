from django.urls import path

from .views import HomeSiteView

app_name = 'core'
urlpatterns = [
    path('', HomeSiteView.as_view(), name="home_admin"),

]
