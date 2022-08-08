from django.shortcuts import render
from .models import Card
from django.views import View
from django.views.generic import (
    ListView,
)

# Create your views here.
#class Home(View):
    #def get(self, request):
        #return render(request, "cards/base.html")

class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")