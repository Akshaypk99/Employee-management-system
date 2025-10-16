"""
URL configuration for employee_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('api/auth/', include('authentication.urls')),
    path('api/', include('employee.urls')),
    # html
    path('', TemplateView.as_view(template_name='login.html'), name='login'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('forms/', TemplateView.as_view(template_name='form_builder.html'), name='form_builder'),
    path('forms/<int:id>/edit/', TemplateView.as_view(template_name='form_edit.html'), name='form_edit'),
    path('employees/list/', TemplateView.as_view(template_name='employee_list.html'), name='employee_list'),
    path('employees/create/', TemplateView.as_view(template_name='employee_create.html'), name='employee_create'),
    path('employees/edit/<int:id>/', TemplateView.as_view(template_name='employee_edit.html'), name='employee_edit'),


]
