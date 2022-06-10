from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Message
# Create your views here.


class MainPageView(TemplateView):
    template_name: str = "index.html"


def allmessagesview(request):
    template_name = "messages.html"
    messages = Message.objects.all()
    return render(request, template_name, {'messages':messages})