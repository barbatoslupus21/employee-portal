from django.contrib import admin
from .models import FinanceType, Loan, Savings, Medicine, PerfectAttendance, EmployeePayslip

admin.site.register(FinanceType)
admin.site.register(Loan)
admin.site.register(Savings)
admin.site.register(Medicine)
admin.site.register(PerfectAttendance)
admin.site.register(EmployeePayslip)
