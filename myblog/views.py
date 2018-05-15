from django.shortcuts import render
from .models import Category,Post,Tag
from django.views.generic.list import ListView
from django.http import HttpResponse
import markdown2
# Create your views here.

def index (request):
    return HttpResponse("welcome")
