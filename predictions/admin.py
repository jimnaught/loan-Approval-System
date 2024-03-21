from django.contrib import admin
from .models import LoanApplication

# Register your models here.
@admin.register(LoanApplication)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'loan_amount', 'gender', 'married', 'dependents', 'education', 'self_employed', 'applicant_income', 'co_applicant_income', 'loan_amount_term', 'credit_history', 'property_area')

