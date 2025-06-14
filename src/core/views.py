from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # автоматично залогінюємо нового користувача
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    if request.user.is_authenticated:
        # Показуємо домашню сторінку з меню для залогінених
        return render(request, 'home.html')
    else:
        # Якщо не залогінений — показуємо форму логіну і обробляємо POST для логіну
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('home')
        else:
            form = AuthenticationForm()
        return render(request, 'login_home.html', {'form': form})

@login_required
def linux_info(request):
    return render(request, 'linux.html', {'title': 'Основи Linux'})

@login_required
def network_info(request):
    return render(request, 'network.html')

@login_required
def logging_monitoring_info(request):
    return render(request, 'logging_monitoring.html')

@login_required
def cloud_providers_info(request):
    return render(request, 'cloud_providers.html')

@login_required
def ci_cd_info(request):
    return render(request, 'ci_cd.html')

@login_required
def security_info(request):
    return render(request, 'security.html')


