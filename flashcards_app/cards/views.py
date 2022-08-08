from django.shortcuts import render
from .models import Card
from django.views import View

# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, "cards/base.html")