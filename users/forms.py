from django import forms
from . models import Customer,CustomerPolicy,CustPolDocs,PremiumSchedules,PremiumPayment,Complaints
from  company.models import State, District

from login.models import CustomerRegistration


class customerform(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        widget=forms.RadioSelect,
        required=True
    )


    #date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Customer
        fields = [
            'customer_id', 'customer_name', 'address', 'phone', 'email_id',
            'stateid', 'distid', 'city', 'dob', 'gender'
              # only the essentials
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class customerpolicyform(forms.ModelForm):
    reg_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = CustomerPolicy
        fields = "__all__"

class customerdocform(forms.ModelForm):
    class Meta:
        model = CustPolDocs
        fields = "__all__"

class prescheduleform(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = PremiumSchedules
        fields = "__all__"

class prepayform(forms.ModelForm):
    class Meta:
        model = PremiumPayment
        fields = "__all__"


class compform(forms.ModelForm):
    #comp_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    #act_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Complaints
        fields = ['comp_type', 'complaint']


#buypolicyfrom
class BuyPolicyForm(forms.ModelForm):
    date=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = CustomerRegistration
        fields = ['qualification', 'occupation','height','weight','physical_status','health_condition','business_status','identification_mark',
                  'identity_proof','nominee_name','nom_rel','payment_mode','credit_card_no','photo','date']
        exclude = ['customer_id', 'policy_id', 'Login', 'policy_status']

#documentform
class UploadDocumentsForm(forms.ModelForm):
    class Meta:
        model=CustPolDocs
        fields = ['documents']


#premiumpaymentstartform
class PremiumForm(forms.ModelForm):
    class Meta:
        model=CustomerRegistration
        fields = ['email_id','phone','dob']

#companyReply
class CompReplyForm(forms.ModelForm):
    act_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Complaints
        fields = ['action', 'act_date', 'comp_status']

#editprofile
class EditProfileForm(forms.ModelForm):
    class Meta:
        model=CustomerRegistration
        fields=['address','phone','email_id','city','occupation','weight','nominee_name','nom_rel']