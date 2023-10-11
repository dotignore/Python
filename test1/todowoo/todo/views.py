from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signupuser(request):
    return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})