from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'expenses/index.html')


def AddExpenses(request):
    return render(request, 'expenses/add_expenses.html')