from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import utils
from django.contrib import messages
from .forms import LoanApplicationForm
from .models import LoanApplication


# Create your views here.
@login_required
def home(request):
    sample = utils.prepare_input_data_for_model(1, 1, 0, 0, 1,
                                              100, 0, 1000, 3, 0, 2)

    pp = utils.loaded_model_LR.predict(sample)
    print(pp)

    pp2 = utils.loaded_model_RF.predict(sample)
    print(pp2)

    context = {

    }

    return render(request, 'index.html', context)


@login_required
def apply(request):
    
    if request.method == 'POST':
        form = LoanApplicationForm(data=request.POST)

        if form.is_valid():
            new_application = form.save(commit=False)
            new_application.user = request.user
            
            # Compute here
            sample = utils.prepare_input_data_for_model(new_application.gender, new_application.married, new_application.dependents, new_application.education, new_application.self_employed,
                                              new_application.applicant_income, new_application.co_applicant_income, new_application.loan_amount, new_application.loan_amount_term, new_application.credit_history, new_application.property_area)

            pp = utils.loaded_model_LR.predict(sample)

            if pp == 1:
                messages.success(request, "Loan Application Approved")
                new_application.status = 'Approved'
                new_application.save()

            if pp == 0:
                messages.error(request, 'Loan Application Declined')
                new_application.status = 'Declined'
                new_application.save()

            print('/////')
            print(pp)


            # Give message
            
            return redirect('predictions:applications')
        messages.error(request, 'Form not valid')
    else:
        form = LoanApplicationForm()

    context = {
        'form': form
    }

    return render(request, 'predictions/apply.html', context)

@login_required
def applications(request):

    applications = LoanApplication.objects.filter(user=request.user).order_by('-date_created')
  
    context = {
        'applications': applications
    }

    return render(request, 'predictions/applications.html', context)


    
