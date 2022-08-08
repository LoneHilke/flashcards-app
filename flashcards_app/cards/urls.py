from django.urls import path
from .views import Home

urlpatterns = [
    #path("", TemplateView.as_view(template_name="cards/base.html"), name="home"),
    path("", Home.as_view(), name="home"),
]