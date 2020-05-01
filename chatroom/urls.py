from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('send_message', views.store_message,name='store_message'),
    path('fetch_message', views.message_fetch,name='fetch_message'),
]