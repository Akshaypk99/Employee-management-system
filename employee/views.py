
# Create your views here.
from rest_framework import generics, permissions
from .models import Employee, FormTemplate
from .serializers import EmployeeSerializer, FormTemplateSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    # queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = Employee.objects.all()
        search = self.request.query_params.get("search", None)
        if search:
            queryset = [emp for emp in queryset if search.lower() in str(emp.data).lower()]
        return queryset

    # add user info while creating employee::
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    

class EmployeeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class FormTemplateListCreateView(generics.ListCreateAPIView):
    queryset = FormTemplate.objects.all()
    serializer_class = FormTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]

class FormTemplateRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormTemplate.objects.all()
    serializer_class = FormTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]
