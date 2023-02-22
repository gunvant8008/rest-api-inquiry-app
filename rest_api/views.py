from rest_framework import viewsets
from rest_framework import permissions
from .models import Inquiry, Bill, BillDetails, Employee, Product
from .serializers import InquirySerializer, BillSerializer, BillDetailsSerializer, EmployeeSerializer, ProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class InquiryViewSet(viewsets.ModelViewSet):
    queryset=Inquiry.objects.all()
    serializer_class= InquirySerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]

class BillViewSet(viewsets.ModelViewSet):
    queryset=Bill.objects.all()
    serializer_class= BillSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]

class BillDetailsViewSet(viewsets.ModelViewSet):
    queryset=BillDetails.objects.all()
    serializer_class= BillDetailsSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class= EmployeeSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class= ProductSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]