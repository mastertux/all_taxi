from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import logout

def index(request):
    return render(request, 'dashboard/index.html', context=None)
