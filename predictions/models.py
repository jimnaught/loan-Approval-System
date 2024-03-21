from django.db import models
from django.contrib.auth.models import User

GENDER = (
    ("Gender", "Gender"),
    ("Male", "Male"),
    ("Female", "Female"),
)

MARRIED = (
    ("Married", "Married"),
    ("Yes", "Yes"),
    ("No", "No"),
)

DEPENDENTS = (
    ("Dependents", "Dependents"),
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("More than 2", "More than 2"),

)

EDUCATION = (
    ("Education", "Education"),
    ("Graduate", "Graduate"),
    ("Not Graduate", "Not Graduate"),
)

SELF_EMPLOYED = (
    ("Self Employed", "Self Employed"),
    ("Yes", "Yes"),
    ("No", "No"),
)

PROPERTY_AREA = (
    ("Area", "Area"),
    ("Urban", "Urban"),
    ("Rural", "Rural"),
    ("Semi Urban", "Semi Urban"),
)

CREDIT_HISTORY = (
    ("Credit History", "Credit History"),
    ("0", "0"),
    ("1", "1"),
)

STATUS = (
    ("Approved", "Approved"),
    ("Declined", "Declined"),
)

class LoanApplication(models.Model):
    gender = models.CharField(max_length=50, choices=GENDER)
    married = models.CharField(max_length=50, choices=MARRIED)
    dependents = models.CharField(max_length=50, choices=DEPENDENTS)
    education = models.CharField(max_length=50, choices=EDUCATION)
    self_employed = models.CharField(max_length=50, choices=SELF_EMPLOYED)
    applicant_income = models.IntegerField(default=0)
    co_applicant_income = models.IntegerField(default=0)
    loan_amount = models.IntegerField(default=0)
    loan_amount_term = models.IntegerField(default=0)
    credit_history = models.CharField(max_length=50, choices=CREDIT_HISTORY)
    property_area = models.CharField(max_length=50, choices=PROPERTY_AREA)
    status = models.CharField(max_length=50, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")

