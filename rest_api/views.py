from rest_framework import viewsets
from rest_framework import permissions
from .models import Inquiry, Bill, BillDetails, Employee, Product
from .serializers import InquirySerializer, BillSerializer, BillDetailsSerializer, EmployeeSerializer, ProductSerializer

# Create your views here.
class InquiryViewSet(viewsets.ModelViewSet):
    queryset=Inquiry.objects.all()
    serializer_class= InquirySerializer
    permission_classes=[permissions.IsAuthenticated]

class BillViewSet(viewsets.ModelViewSet):
    queryset=Bill.objects.all()
    serializer_class= BillSerializer
    permission_classes=[permissions.IsAuthenticated]

class BillDetailsViewSet(viewsets.ModelViewSet):
    queryset=BillDetails.objects.all()
    serializer_class= BillDetailsSerializer
    permission_classes=[permissions.IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class= EmployeeSerializer
    permission_classes=[permissions.IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class= ProductSerializer
    permission_classes=[permissions.IsAuthenticated]