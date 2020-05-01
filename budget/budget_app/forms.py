from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BudgetInfo, Expense


class BudgetForm(forms.ModelForm):
    
    class Meta:
        model = BudgetInfo
        fields = ['name', 'budget']


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ['title', 'date', 'price', 'category']
        widgets = {'date': forms.DateInput()}


class SignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']