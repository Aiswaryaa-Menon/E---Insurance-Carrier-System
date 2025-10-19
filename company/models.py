from django.db import models

from login.models import CustomerRegistration

class State(models.Model):
    stateid = models.AutoField(primary_key=True)
    stname = models.CharField(max_length=25, null=False)

    def __str__(self):
        return f"ID: {self.stateid} - {self.stname}"


class District(models.Model):
    distid = models.AutoField(primary_key=True)
    distname = models.CharField(max_length=25, null=False)
    state = models.ForeignKey('company.State', on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return f"ID: {self.distid} - {self.distname}"


class CompanyBranches(models.Model):
    Branch_Id = models.AutoField(unique=True, primary_key=True)
    Company_Id = models.CharField(max_length=25, null=False, unique=True)
    BranchName = models.CharField(max_length=25, null=False)
    BAddress = models.CharField(max_length=50, null=False, unique=True)
    emailid = models.EmailField(max_length=25, null=False, unique=True)
    state = models.ForeignKey('company.State', on_delete=models.CASCADE, related_name='branches')
    district = models.ForeignKey('company.District', on_delete=models.CASCADE)
    City = models.CharField(max_length=25, null=False)
    Phone = models.BigIntegerField(null=False, unique=True)

    def __str__(self):
        return f"ID: {self.Branch_Id} - {self.BranchName}"

class Insurance_Type(models.Model):
    InsType_Id = models.AutoField(primary_key=True)
    Ins_Type = models.CharField(max_length=25, null=False)

    def __str__(self):
        return self.Ins_Type

class Claim_Status(models.Model):
    CStatusCode = models.AutoField(primary_key=True)
    CStatus_Choices = [
        ('', 'Select'),
        ('New Claim', 'New Claim'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('In Review', 'In Review'),
    ]
    CStatus = models.CharField(
        max_length=25,
        choices=CStatus_Choices,
        default='',
        help_text="Select the current claim status"
    )

    def __str__(self):
        return self.CStatus


class Sum_Assured(models.Model):
    sum_assureid = models.AutoField(primary_key=True)
    sum_assured = models.BigIntegerField(null=False)

    def __str__(self):
        return f"ID: {self.sum_assureid} - {self.sum_assured}"


class News(models.Model):
    newsid = models.AutoField(primary_key=True)
    news_title=models.CharField(max_length=100,null=False)
    news = models.CharField(max_length=500, null=False)
    post_date = models.DateField(null=False)
    STATUS_CHOICES = [
        ('','Select'),
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived')
    ]
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='',
        help_text="News Status"
    )

class Policies(models.Model):
    Policy_Id = models.AutoField(primary_key=True)
    insurance_type = models.ForeignKey('company.Insurance_Type', on_delete=models.CASCADE)
    PolicyName = models.CharField(max_length=25, null=False)
    PolStDate = models.DateField(null=False)
    Age_at_entry = models.IntegerField(null=False)
    max_age = models.IntegerField(null=False)
    sum_assured = models.BigIntegerField(null=True)
    policy_term =  models.TextField(null=False)
    PolStatus = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f"{self.Policy_Id} - {self.PolicyName}"

class Policy_Features(models.Model):
    Feature_Id = models.AutoField(primary_key=True)
    policyid = models.ForeignKey('company.Policies', on_delete=models.CASCADE, related_name='features')
    Feature_title = models.CharField(max_length=200, null=False)
    Feature_Descr = models.TextField(null=False)

    def __str__(self):
        return f"{self.policyid.Policy_Id} - {self.Feature_title}"

class Policy_Benefits(models.Model):
    Benefit_id = models.AutoField(primary_key=True)
    policyid = models.ForeignKey('company.Policies', on_delete=models.CASCADE, related_name='benefits')
    Benefit = models.CharField(max_length=25, null=False)
    Descr = models.TextField(null=False)

    def __str__(self):
        return f"{self.policyid.Policy_Id} - {self.Benefit}"

class Policy_Documents(models.Model):
    Docu_Id = models.AutoField(primary_key=True)
    policyid = models.ForeignKey('company.Policies', on_delete=models.CASCADE, related_name='documents')
    Docu_Name = models.CharField(max_length=25, null=False)
    Docu_File = models.FileField(
        upload_to='policy_documents/',
        null=True,
        blank=True,
        help_text="Upload policy document file (PDF, DOCX, etc.)"
    )

    def __str__(self):
        return f"{self.Docu_Name} (ID: {self.Docu_Id})"

class Premium_Mode(models.Model):
    pre_mode_id = models.AutoField(primary_key=True)
    PREMIUM_CHOICES = [
        ('','Select'),
        ('Quarterly', 'Quarterly'),
        ('Half-Yearly', 'Half-Yearly'),
        ('Yearly', 'Yearly'),

    ]
    pre_mode = models.CharField(
        max_length=25,
        choices=PREMIUM_CHOICES,
        default='',
        help_text="Select the premium payment mode"
    )

    def __str__(self):
        return f"ID: {self.pre_mode_id} - {self.pre_mode}"


class Policy_Commission(models.Model):
    PolComId = models.AutoField(primary_key=True)
    policyid = models.ForeignKey('company.Policies', on_delete=models.CASCADE, related_name='commission')
    Comm_For_Yrs = models.IntegerField(null=False)
    Comm_Rate = models.CharField(max_length=25, null=False)

class Policy_Premium(models.Model):
    pol_pre_id = models.AutoField(primary_key=True)
    pol_Premium = models.FloatField(null=False)
    policyid = models.ForeignKey('company.Policies', on_delete=models.CASCADE,null=True)
    premode=models.ForeignKey('company.Premium_Mode',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.pol_Premium} (ID: {self.pol_pre_id})"

class Claims(models.Model):
    claim_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('login.CustomerRegistration', on_delete=models.CASCADE)
    policy_id = models.ForeignKey('company.Policies', on_delete=models.CASCADE)
    cstatus_code=models.ForeignKey('company.Claim_Status',on_delete=models.CASCADE,null=True)
    claim_date = models.DateField(auto_now_add=True,blank=True)
    purpose = models.CharField(max_length=200)
    claim_amt = models.FloatField()
    approval_amt = models.FloatField(null=True)
    app_date = models.DateField(null=True,blank=True)
    Invoice =models.FileField(upload_to='invoice_documents/',null=False,help_text='Upload Hospital Bills/Pharmacy Bills/Diagnostic Reports')
    Bank_Details =models.FileField(upload_to='Bank_Details/',null=False,help_text='Upload Cancelled Cheque/Passbook Front Page')
    Identity_Proof =models.FileField(upload_to='ID/',null=False,help_text='Upload Aadhar card/Pan Card/Voter ID/Driving License')
    PAY_STATUS_CHOICES = [
        ('','Select'),
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Paid', 'Paid')
    ]
    pay_status = models.CharField(
        max_length=30,
        choices=PAY_STATUS_CHOICES,
        default='',
        help_text="Select the payment status"
    )

    def __str__(self):
        return f"Claim {self.claim_id} - {self.cstatus_code}"
