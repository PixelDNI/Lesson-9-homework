from django.shortcuts import render
from .models import User
# Create your views here.
def main(request):
    context = {'users': User.objects.all()}
    return render(request, 'index.html', context)

def more(request, user):
    context = {'user': User.objects.get(id=user)}
    return render(request, 'user.html', context)