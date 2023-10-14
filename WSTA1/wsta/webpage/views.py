from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def firstpage(request):
    request.method == 'GET'
    return render(request, 'frontpage/firstpage.html')
    # else:
    #     if request.POST['']:
    #     else:

# def signupuser(request):
#     if request.method == 'GET':
#         return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
#                 user.save()
#                 login(request, user)
#                 return redirect('currenttodos')
#             except IntegrityError:
#                 return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
#         else:
#             return render(request, 'todo/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})
