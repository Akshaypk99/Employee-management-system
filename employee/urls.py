from django.urls import path
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDeleteView, FormTemplateListCreateView, FormTemplateRetrieveUpdateDeleteView
from django.views.generic import TemplateView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDeleteView.as_view(), name='employee-detail'),

    path('forms/', FormTemplateListCreateView.as_view(), name='form-list-create'),
    path('forms/<int:pk>/', FormTemplateRetrieveUpdateDeleteView.as_view(), name='form-detail'),
    
    
]
