from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')

                else:
                    return HttpResponse('disabled account')
            else:
                return HttpResponse('Invalid login')

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
