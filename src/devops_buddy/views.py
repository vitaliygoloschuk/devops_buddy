from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def network_info(request):
    return render(request, 'network.html')

def linux_info(request):

    return render(request, 'linux.html')

def logging_monitoring_info(request):
    return render(request, 'logging_monitoring.html', {'title': 'Логування та Моніторинг'})

def cloud_providers_info(request):
    return render(request, 'cloud_providers.html')

def ci_cd_info(request):
    return render(request, 'ci_cd.html')