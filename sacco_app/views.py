from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from .forms import CreditRiskForm
#from .your_ml_module import predict_credit_risk  # Import your machine learning model function

def home(request):

    return render(request, 'home.html')
