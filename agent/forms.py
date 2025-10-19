from django import forms

from  agent.models import Agent_Policy
from company.models import State, District
from login.models import CustomerRegistration






class agentpolform(forms.ModelForm):
    ModDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Agent_Policy
        fields = "__all__"

class AgentBuyPolicyForm(forms.Form):
    customer_id = forms.ModelChoiceField(
        queryset=CustomerRegistration.objects.all(),
        empty_label="Select Customer",
        to_field_name="customer_id",
        required=True,
        label="Select Customer"
    )

    qualification = forms.CharField(required=False)
    occupation = forms.CharField(required=False)
    height = forms.FloatField(required=False)
    weight = forms.FloatField(required=False)
    physical_status = forms.CharField(required=False)
    health_condition = forms.CharField(required=False)
    business_status = forms.CharField(required=False)
    identification_mark = forms.CharField(required=False)
    identity_proof = forms.FileField(required=False)
    nominee_name = forms.CharField(required=False)
    nom_rel = forms.CharField(required=False)
    payment_mode = forms.CharField(required=False)
    credit_card_no = forms.CharField(required=False)
    photo = forms.FileField(required=False)
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))