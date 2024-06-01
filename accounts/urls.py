from django.urls import path
from accounts.views import SingUp


urlpatterns = [
    path('singup',SingUp.as_view(), name='singup'),
    
]