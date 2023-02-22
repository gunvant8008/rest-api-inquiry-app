from rest_framework import serializers
from .models import Inquiry, Bill, BillDetails, Employee, Product

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ['id', 'company_name', 'company_owner', 'manager', 'address', 'contact_no', 'email', 'added_on', 'is_member', 'is_active_member']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'buy_price', 'sell_price', 'c_gst', 's_gst', 'description', 'added_on']

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'customer_id', 'added_on']

class BillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillDetails
        fields = ['id', 'bill_id','product_id', 'added_on']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'joining_date','phone','address', 'added_on']

