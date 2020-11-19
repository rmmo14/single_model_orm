from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def adduser(request):
    context = {
        'all_users': User.objects.all()
    }
    print(context)
    return render(request, "index.html", context)