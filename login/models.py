from django.db import models
from django.contrib.auth.models import User
#from company.models import State, District
from django.utils.timezone import now



# Create your models here.
class RoleModel(models.Model):
    Role = models.CharField(max_length=20)
    Login = models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.Role} - {self.Login.username}"

#REGISTRATION MODEL FOR AGENT
class AgentRegistration(models.Model):
    Agent_id = models.AutoField(primary_key=True)
    AllocBranch = models.ForeignKey('company.CompanyBranches',on_delete=models.CASCADE)
    Agent_Fname = models.CharField(max_length=25, null=False)
    Agent_Lname = models.CharField(max_length=25, null=False)
    code = models.CharField(max_length=15, null=False)
    Address_line1 = models.CharField(max_length=50, null=False)
    Address_line2 = models.CharField(max_length=50, null=False)
    stateid = models.ForeignKey('company.State', on_delete=models.CASCADE, related_name='login_state')
    distid = models.ForeignKey('company.District', on_delete=models.CASCADE, related_name='login_district')
    Location = models.CharField(max_length=25, null=False)
    Phone = models.CharField(max_length=15, null=False)
    Email_id = models.EmailField(max_length=50,null=False)
    Photo = models.ImageField(upload_to='agent_photos/', null=True, blank=True)
    Qualific_Choices = [
        ('', 'Select'),
        ('High School', 'High School'),
        ('Diploma', 'Diploma'),
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
        ('Doctorate', 'Doctorate')
    ]
    Qualification = models.CharField(
        max_length=30,
        choices=Qualific_Choices,
        default='',
        help_text="Select the user's highest qualification"
    )
    DOB = models.DateField(null=False)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=False)
    Experience =models.IntegerField(null=False, help_text="Enter years of experience")
    AGENT_TYPE_CHOICES = [
        ('','Select'),
        ('Independent', 'Independent Agent'),
        ('Corporate', 'Corporate Agent'),
        ('Broker', 'Broker'),
        ('Tied', 'Tied Agent'),
        ('General', 'General Agent'),
        ('Specialist', 'Specialist Agent'),
    ]

    Type = models.CharField(
        max_length=30,
        choices=AGENT_TYPE_CHOICES,
        default='',
        help_text="Select status"
    )

    # Replacing Username & Password with Login reference
    Login = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Pending', 'Pending'),
    ]

    Status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="",
        help_text="Current status of the agent"
    )

    RegDate = models.DateField(default=now, null=False)

    def __str__(self):
        return f"{self.Agent_Fname} {self.Agent_Lname}"


class CustomerRegistration(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=25, null=False)
    address = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=20,null=True)
    email_id = models.EmailField(max_length=25, null=False)
    stateid = models.ForeignKey('company.State', on_delete=models.CASCADE, related_name='customer_state',null=True)
    distid = models.ForeignKey('company.District', on_delete=models.CASCADE, related_name='customer_district',null=True)
    city = models.CharField(max_length=25, null=False)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=10, null=True)
    Qualific_Choices = [
        ('', 'Select'),
        ('High School', 'High School'),
        ('Diploma', 'Diploma'),
        ('Bachelor', 'Bachelor'),
        ('Masters', 'Masters'),
        ('Doctorate', 'Doctorate')
    ]
    qualification = models.CharField(
        max_length=30,
        choices=Qualific_Choices,
        default='',
        null=True,
        help_text="Select the user's highest qualification"
    )
    occupation = models.CharField(max_length=20, null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
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
        null=True,
        help_text="Select status"
    )
    HEALTH_CONDITION_CHOICES = [
        ('', 'Select'),
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
        null=True,
        help_text="Select status"
    )
    BUSINESS_STATUS_CHOICES = [
        ('', 'Select'),
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
        null=True,
        help_text="Select status"
    )
    identification_mark = models.CharField(max_length=30, null=True)
    identity_proof = models.ImageField(
        upload_to='identity_proof/',
        null=True,
        blank=True,
        help_text="Upload Identity Proof(Aadhaar, Passport, etc)"
    )
    nominee_name = models.CharField(max_length=25, null=True)
    nom_rel = models.CharField(max_length=20, null=True)
    payment_mode = models.CharField(max_length=20, null=True)
    credit_card_no = models.BigIntegerField(null=True)
    photo = models.ImageField(upload_to='customer_photos/', null=True, blank=True)
    date = models.DateField(null=True)  # Capture registration date automatically
    STATUS_CHOICES = [
        ('', 'Select'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
        ('closed', 'Closed')
    ]
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='',
        null=True,
        help_text="Select status"
    )

    #  Added Login Field (One-to-One with User)
    Login = models.OneToOneField(User, on_delete=models.CASCADE,related_name='customer',null=False)

    def __str__(self):
        return f"{self.customer_id} - {self.customer_name}"


