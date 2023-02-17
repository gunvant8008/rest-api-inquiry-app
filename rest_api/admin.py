from django.contrib import admin
from .models import Inquiry, Product, Bill, BillDetails, Employee
# Register your models here.

class InquiryAdmin(admin.ModelAdmin):
    list_display=('company_name', 'address', 'email')

class ProductAdmin(admin.ModelAdmin):
    list_display=('name', 'description', 'sell_price')
class BillAdmin(admin.ModelAdmin):
    list_display=('id', 'customer_id', 'added_on')

class BillDetailsAdmin(admin.ModelAdmin):
    list_display=('id', 'bill_id', 'added_on')

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'phone', 'added_on')
admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(BillDetails, BillDetailsAdmin)
admin.site.register(Employee, EmployeeAdmin)