from django import forms
from .models import CompanyBranches, State, District, Insurance_Type, Claim_Status, Policies, Policy_Features,Policy_Benefits, Policy_Documents, Premium_Mode, Policy_Commission,Policy_Premium,Sum_Assured,News,Claims


class companyform(forms.ModelForm):
    class Meta:
        model = CompanyBranches
        fields = "__all__"

class stateform(forms.ModelForm):
    class Meta:
        model = State
        fields = ('stateid','stname')

class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields="__all__"

class insurancetypeform(forms.ModelForm):
    class Meta:
        model = Insurance_Type
        fields = ('InsType_Id','Ins_Type')
        labels= {
            'Ins_Type': 'Insurance Type',
        }


class claimstatusform(forms.ModelForm):
    class Meta:
        model = Claim_Status
        fields = ('CStatusCode','CStatus')


class PolicyForm(forms.ModelForm):
    PolStDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Policies
        fields="__all__"
        widgets = {
            'PolStatus': forms.RadioSelect(choices=[
                ('Active', 'Active'),
                ('Inactive', 'Inactive'),
                ('Pending', 'Pending'),
            ]),
            'policy_term': forms.Textarea(attrs={'rows': 3, 'cols': 30}),
        }
        labels = {
            'insurance_type': 'Insurance Type',
            'PolicyName': 'Policy Name',
            'PolStDate': 'Policy Start Date',
            'Age_at_entry': 'Minimum Age at Entry',
            'max_age': 'Maximum Age',
            'Min_sum_assurid': 'Minimum Sum Assured',
            'max_sum_assureid': 'Maximum Sum Assured',
            'policy_term': 'Policy Term',
            'PolStatus': 'Policy Status',
        }

class policyfeatureform(forms.ModelForm):
    class Meta:
        model = Policy_Features
        fields ="__all__"

    widgets = {
        'Feature_Descr': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
    }

class policybenefitsform(forms.ModelForm):
    class Meta:
        model = Policy_Benefits
        fields ="__all__"

        labels={
            'Descr':'Description',
        }

class policydocumentsform(forms.ModelForm):
    class Meta:
        model = Policy_Documents
        fields ="__all__"

class preform(forms.ModelForm):
    class Meta:
        model = Premium_Mode
        fields = "__all__"

class pcform(forms.ModelForm):
    class Meta:
        model = Policy_Commission
        fields ="__all__"

class polpreform(forms.ModelForm):
    class Meta:
        model = Policy_Premium
        fields ="__all__"

class sumform(forms.ModelForm):
    class Meta:
        model = Sum_Assured
        fields ="__all__"

class newsform(forms.ModelForm):
    post_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = News
        fields ="__all__"

class claimform(forms.ModelForm):
    class Meta:
        model = Claims
        fields =('policy_id','purpose','claim_amt','Invoice','Bank_Details','Identity_Proof')
        exclude = ['claim_date', 'app_date','cstatus_code']

