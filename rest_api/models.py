from django.db import models

# Create your models here.
class Inquiry(models.Model):
    
    id=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=255)
    company_owner=models.CharField(max_length=255)
    manager=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    contact_no=models.CharField(max_length=255)
    email=models.EmailField(default='')
    description=models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
    # lead_type = models.CharField(max_length=100)
    #source = models.Choices()
    is_member=models.BooleanField(default=False)
    is_active_member=models.BooleanField(default=False)
    #purchases= array of purchased products
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    buy_price=models.CharField(max_length=255)
    sell_price=models.CharField(max_length=255)
    c_gst=models.CharField(max_length=255)
    s_gst=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

class Bill(models.Model):
    id=models.AutoField(primary_key=True)
    customer_id=models.ForeignKey(Inquiry,on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

class BillDetails(models.Model):
    choices=('Debit',"Credit")
    id=models.AutoField(primary_key=True)
    bill_id=models.ForeignKey(Bill,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    joining_date =models.DateField()
    phone=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)
