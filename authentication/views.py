from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

class UsernameValidationView(View):
    def post(self, request):
        #return render(request, 'authentication/register.html')
        data=json.loads(request.body)
        username=data['username']
        
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Sorry, username in use'}, status=409)
        return JsonResponse({'username_valid': True})