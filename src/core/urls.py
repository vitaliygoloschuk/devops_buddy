from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topic/<slug:slug>/', views.topic_detail, name='topic_detail'),
    path('accounts/', include('django.contrib.auth.urls')),  # логін/логаут
    path('signup/', views.signup_view, name='signup'),        # реєстрація
    path('linux/', views.linux_info, name='linux_info'),
    path('network/', views.network_info, name='network_info'),
    path('logging-monitoring/', views.logging_monitoring_info, name='logging_monitoring_info'),
    path('ci-cd/', views.ci_cd_info, name='ci_cd_info'),
    path('cloud-providers/', views.cloud_providers_info, name='cloud_providers_info'),
    path('security/', views.security_info, name='security_info'),

    
]
