import joblib
import numpy as np


def prepare_input_data_for_model(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area):
    if Gender == 'Male':
        Gender = int(1)
    else:
        Gender = int(0)

    if Married == 'Yes' or Married == 'Married':
        Married = 1
    else:
        Married = 0


    if Dependents == '0':
        Dependents = 0
    elif Dependents == '1':
        Dependents = 1
    elif Dependents == '2':
        Dependents = 2
    else:
        Dependents = 3


    if Education == 'Graduate' or Education == 'Education':
        Education = 0
    else:
        Education = 1


    if Self_Employed == 'Yes' or Self_Employed == 'Self Employed':
        Self_Employed = 1
    else:
        Self_Employed = 0

    if Property_Area == 'Urban':
        Property_Area = 2
    elif Property_Area == 'Rural':
        Property_Area = 0
    else:
        Property_Area = 1

    Features = [Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome,
         CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]
    sample = np.array(Features, dtype=int).reshape(-1, len(Features))

    print(sample)


    return sample



loaded_model_LR = joblib.load(open("loan_predition_model_LR.pkl", 'rb'))
loaded_model_RF = joblib.load(open("loan_predition_model_RF", 'rb'))




