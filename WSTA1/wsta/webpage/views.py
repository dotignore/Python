from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def firstpage(request):
    return render(request, 'frontpage/firstpage.html')