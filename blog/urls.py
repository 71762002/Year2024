from django.urls import path

from .views import home, tabriklar, images



urlpatterns = [
    path("", home, name='home'),
    path("tabriklar_siz_uchun/", tabriklar, name='tabriklar'),
    path("images/", images, name='images'),
]