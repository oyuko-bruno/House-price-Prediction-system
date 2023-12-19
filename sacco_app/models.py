from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# models.py
from django.db import models

class CreditRiskInput(models.Model):
    purpose_choices = [
        ('radio/TV', 'Radio/TV'),
        ('education', 'Education'),
        ('furniture/equipment', 'Furniture/Equipment'),
        ('car', 'Car'),
        ('business', 'Business'),
        ('domestic appliances', 'Domestic Appliances'),
        ('repairs', 'Repairs'),
        ('vacation/others', 'Vacation/Others'),
    ]

    sex_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    housing_choices = [
        ('own', 'Own'),
        ('free', 'Free'),
        ('rent', 'Rent'),
    ]

    saving_accounts_choices = [
        ('nun', 'NuN'),
        ('little', 'Little'),
        ('quite rich', 'Quite Rich'),
        ('rich', 'Rich'),
        ('moderate', 'Moderate'),
    ]

    checking_account_choices = [
        ('little', 'Little'),
        ('moderate', 'Moderate'),
        ('nun', 'NuN'),
        ('rich', 'Rich'),
    ]

    age_cat_choices = [
        ('Senior', 'Senior'),
        ('Student', 'Student'),
        ('Adult', 'Adult'),
        ('Young', 'Young'),
    ]

    purpose = models.CharField(max_length=50, choices=purpose_choices)
    sex = models.CharField(max_length=10, choices=sex_choices)
    housing = models.CharField(max_length=10, choices=housing_choices)
    saving_accounts = models.CharField(max_length=15, choices=saving_accounts_choices)
    checking_account = models.CharField(max_length=15, choices=checking_account_choices)
    age_cat = models.CharField(max_length=10, choices=age_cat_choices)
