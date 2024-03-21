from django import forms
from .models import LoanApplication, GENDER, MARRIED, DEPENDENTS, EDUCATION, SELF_EMPLOYED, PROPERTY_AREA, CREDIT_HISTORY


class LoanApplicationForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=GENDER, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    married = forms.ChoiceField(choices=MARRIED, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    dependents = forms.ChoiceField(choices=DEPENDENTS, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    education = forms.ChoiceField(choices=EDUCATION, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    self_employed = forms.ChoiceField(choices=SELF_EMPLOYED, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    applicant_income = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'price',
            'placeholder': 'Applicant Income',
        }
    ))

    co_applicant_income = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'price',
            'placeholder': 'Co Applicant Income',
        }
    ))

    loan_amount = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'price',
            'placeholder': 'Loan Amount',
        }
    ))

    loan_amount_term = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'price',
            'placeholder': 'Loan Amount Term',
        }
    ))

    credit_history = forms.ChoiceField(choices=CREDIT_HISTORY, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    property_area = forms.ChoiceField(choices=PROPERTY_AREA, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = LoanApplication
        fields = ('gender', 'married', 'dependents', 'education', 'self_employed', 'applicant_income', 'co_applicant_income', 'loan_amount', 'loan_amount_term', 'credit_history', 'property_area' )
