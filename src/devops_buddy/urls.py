from django.urls import path, include
from core import views  # імпортуємо views з core

urlpatterns = [
    path('', views.home, name='home'),
    path('network/', views.network_info, name='network_info'),
    path('linux/', views.linux_info, name='linux_info'),
    path('logging-monitoring/', views.logging_monitoring_info, name='logging_monitoring_info'),
    path('accounts/signup/', views.signup_view, name='signup'),   # реєстрація
    path('accounts/', include('django.contrib.auth.urls')),       # логін/логаут
    path('linux/', views.linux_info, name='linux_info'),
    path('ci-cd/', views.ci_cd_info, name='ci_cd_info'),
    path('cloud-providers/', views.cloud_providers_info, name='cloud_providers_info'),
    path('security/', views.security_info, name='security_info'),
]
