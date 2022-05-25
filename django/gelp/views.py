from django.shortcuts import render
from .models import HomeValuess



def home(request):
     values = HomeValuess.objects.all()
     context = {
        "values": values
     }
     return render(request, "index.html", context)
def about(request):
    return render(request, "about.html")