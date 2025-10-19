from django.db import models
from django.contrib.auth.models import User

import django

from login.models import CustomerRegistration, AgentRegistration
from company.models import Premium_Mode


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=25, null=False)
    address = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=20,null=True)
    email_id = models.EmailField(max_length=25, null=False)
    stateid = models.ForeignKey('company.State', on_delete=models.CASCADE)
    distid = models.ForeignKey('company.District', on_delete=models.CASCADE)
    city = models.CharField(max_length=25, null=False)
    dob = models.DateField(null=False)
    gender = models.CharField(max_length=10, null=True)
    Qualific_Choices = [
        ('', 'Select'),
        ('High School', 'High School'),
        ('Diploma', 'Diploma'),
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
        ('Doctorate', 'Doctorate')
    ]
    qualification = models.CharField(
        max_length=30,
        choices=Qualific_Choices,
        default='',
        help_text="Select the user's highest qualification",
        null=True

    )
    occupation = models.CharField(max_length=20, null = True)
    height = models.IntegerField(null = True)
    weight = models.IntegerField(null = True)
    PHYSICAL_STATUS_CHOICES = [
        ('', 'Select'),
        ('normal', 'Normal'),
        ('disabled', 'Disabled'),
        ('partially_disabled', 'Partially Disabled'),
        ('amputee', 'Amputee'),
        ('other', 'Other')
    ]
    physical_status = models.CharField(
        max_length=30,
        choices=PHYSICAL_STATUS_CHOICES,
        default='',
        help_text="Select status",
        null=True,

    )
    HEALTH_CONDITION_CHOICES = [
        ('','Select'),
        ('healthy', 'Healthy'),
        ('chronic_illness', 'Chronic Illness'),
        ('heart_disease', 'Heart Disease'),
        ('diabetic', 'Diabetic'),
        ('cancer_history', 'History of Cancer'),
        ('other', 'Other')
    ]
    health_condition = models.CharField(
        max_length=30,
        choices=HEALTH_CONDITION_CHOICES,
        default='',
        help_text="Select status",
        null=True,

    )
    BUSINESS_STATUS_CHOICES = [
        ('','Select'),
        ('employed', 'Employed'),
        ('self_employed', 'Self-Employed'),
        ('unemployed', 'Unemployed'),
        ('retired', 'Retired'),
        ('student', 'Student')
    ]
    business_status = models.CharField(
        max_length=30,
        choices=BUSINESS_STATUS_CHOICES,
        default='',
        help_text="Select status",
        null=True,

    )
    identification_mark = models.CharField(max_length=30, null = True)
    identity_proof  = models.ImageField(
        upload_to='identity_proof/',
        null=True,

        help_text="Upload Identity Proof(Aadhaar, Passport, etc)"
    )
    nominee_name = models.CharField(max_length=25, null = True)
    nom_rel = models.CharField(max_length=20, null = True)
    payment_mode = models.CharField(max_length=20, null = True)
    credit_card_no = models.BigIntegerField(null = True)
    photo = models.ImageField(upload_to='customer_photos/', null=True)
    date = models.DateField(null = True)
    STATUS_CHOICES = [
        ('','Select'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
        ('closed', 'Closed')
    ]
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='inactive',
        help_text="Select status",
        null=True,
    )

    def __str__(self):
        return f"ID: {self.customer_id} - {self.customer_name}"


class CustomerPolicy(models.Model):
    cpol_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('login.CustomerRegistration', on_delete=models.CASCADE)
    agent=models.ForeignKey(AgentRegistration,on_delete=models.CASCADE,null=True,related_name='customerpolicy')
    policy_id = models.ForeignKey('company.Policies', on_delete=models.CASCADE)
    reg_date = models.DateField(default=django.utils.timezone.now)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    premium_amt = models.FloatField(null=True)
    premium_mode=models.ForeignKey('company.Premium_Mode',on_delete=models.CASCADE,null=True)
    POLICY_STATUS_CHOICES = [
        ('','Select'),
        ('approved', 'approved'),
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
        ('pending', 'Pending'),
        ('renewed', 'Renewed')
    ]
    policy_status = models.CharField(
        max_length=30,
        choices=POLICY_STATUS_CHOICES,
        default='pending',
        help_text="Select status"
    )

    def __str__(self):
        return f"{self.customer_id.customer_name} - {self.policy_id}"






class CustPolDocs(models.Model):
    poldoc_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(CustomerRegistration, on_delete=models.CASCADE)
    policy_id = models.ForeignKey('company.Policies', on_delete=models.CASCADE)
    docu_id = models.ForeignKey('company.Policy_Documents', on_delete=models.CASCADE)
    documents = models.FileField(
        upload_to='customer_documents/',
        null=True,
        blank=True,
        help_text="Upload documents"
    )
    DOCUMENT_STATUS_CHOICES = [
        ('','Select'),
        ('submitted', 'Submitted'),
        ('verified', 'Verified'),
        ('rejected', 'Rejected'),
        ('pending_review', 'Pending Review')
    ]
    doc_status = models.CharField(
        max_length=30,
        choices=DOCUMENT_STATUS_CHOICES,
        default='pending_review',
        help_text="Select status"
    )

    def __str__(self):
        return f"PolicyDoc-{self.poldoc_id}"


class PremiumSchedules(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    cpol_id = models.ForeignKey(CustomerPolicy, on_delete=models.CASCADE)
    premium_no = models.CharField(max_length=20, null=False)
    premium_date = models.DateField(null=False)
    due_date = models.DateField(null=False)
    PAY_STATUS_CHOICES = [
        ('','Select'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('overdue', 'Overdue'),
        ('partial', 'Partial Payment')
    ]
    pay_status = models.CharField(
        max_length=30,
        choices=PAY_STATUS_CHOICES,
        default='',
        help_text="Select status")
    pre_mode_id = models.ForeignKey('company.Premium_Mode', on_delete=models.CASCADE)

    def __str__(self):
        return f"Schedule-{self.schedule_id}"


class PremiumPayment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    schedule_id = models.ForeignKey(PremiumSchedules, on_delete=models.CASCADE)
    pay_date = models.DateField(null=False)
    premium_amt = models.FloatField(null=False)
    due_amt = models.FloatField(null=False)
    total_amt = models.FloatField(null=False)

    def __str__(self):
        return f"Payment-{self.payment_id}"


class Complaints(models.Model):
    comp_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(CustomerRegistration, on_delete=models.CASCADE)
    COMPLAIN_TYPE_CHOICES = [
        ('','Select'),
        ('policy_issue', 'Policy Issue'),
        ('payment_problem', 'Payment Problem'),
        ('service_delay', 'Service Delay'),
        ('document_error', 'Document Error'),
        ('other', 'Other')
    ]
    comp_type = models.CharField(
        max_length=20,
        choices=COMPLAIN_TYPE_CHOICES,
        default='',
        help_text="Select status"
    )
    complaint = models.CharField(max_length=30, null=False)
    comp_date = models.DateField(null=False)
    COMPLAIN_ACTION_CHOICES = [
        ('', 'Select'),
        ('investigation', 'Investigation Initiated'),
        ('resolved', 'Resolved'),
        ('pending', 'Pending Further Review'),
        ('escalated', 'Escalated to Higher Authority')
    ]
    action = models.CharField(
        max_length=30,
        null='True',
        choices=COMPLAIN_ACTION_CHOICES,
        default='',
        help_text="Select status"
    )
    act_date = models.DateField(null=True)
    COMPLAIN_STATUS_CHOICES = [
        ('', 'Select'),
        ('received', 'received'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed')
    ]
    comp_status = models.CharField(
        max_length=30,
        null='True',
        choices=COMPLAIN_STATUS_CHOICES,
        default='',
        help_text="Select status"
    )

    def __str__(self):
        return f"Complaint-{self.comp_id}"

