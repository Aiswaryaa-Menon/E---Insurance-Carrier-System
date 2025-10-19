from django import forms
from .models import AgentRegistration,CustomerRegistration
from company.models import State

class AgentRegistrationForm(forms.ModelForm):
    Username=forms.CharField(max_length=50)
    Password=forms.CharField(max_length=50,widget=forms.PasswordInput)
    ConfirmPassword=forms.CharField(max_length=50,widget=forms.PasswordInput)
    Gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        widget=forms.RadioSelect,
        required=True
    )
    class Meta:
        model = AgentRegistration
        exclude = ['Login']
        widgets = {
            'DOB': forms.DateInput(attrs={'type': 'date'}),
            'RegDate': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("Password")
        confirm_password = cleaned_data.get("ConfirmPassword")

        if password and confirm_password and password != confirm_password:
            self.add_error('ConfirmPassword', "Passwords do not match.")

        return cleaned_data

class CustomerRegistrationForm(forms.ModelForm):
    Username = forms.CharField(max_length=50)
    Password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(max_length=50, widget=forms.PasswordInput)
    gender = forms.ChoiceField(
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        widget=forms.RadioSelect,
        required=True
    )
    phone = forms.IntegerField(required=True)
    class Meta:
        model = CustomerRegistration

        fields = [
            'customer_id', 'customer_name', 'address', 'phone', 'email_id',
            'stateid', 'distid', 'city', 'dob', 'gender'

        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }



    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('Password')
        confirm_password = cleaned_data.get('ConfirmPassword')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def clean_identity_proof(self):
        identity_proof = self.cleaned_data.get('identity_proof')
        if identity_proof:
            ext = identity_proof.name.split('.')[-1].lower()
            if ext not in ['pdf', 'jpg', 'jpeg', 'png']:
                raise forms.ValidationError('Invalid file type. Only PDF, JPG, or PNG allowed.')
        return identity_proof