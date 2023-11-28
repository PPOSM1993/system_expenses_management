
from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('validate_username/', csrf_exempt(UsernameValidationView.as_view()), name='validate_username'),
]
