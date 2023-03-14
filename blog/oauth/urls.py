from django.urls import path
from . import auth_view

urlpatterns = [
    path('', auth_view.google_login),
               ]