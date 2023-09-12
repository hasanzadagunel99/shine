from core.views import home, shop

from django.urls import path


urlpatterns = [
    path("", home, name="home"),
    path("", shop, name="home"),
]
