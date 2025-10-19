from django.db import models
from django.utils.timezone import now
from company.models import Policies
from login.models import AgentRegistration

#from e_insurance_carrier.company.models import CompanyBranches


# Update to use lazy imports for models from the 'company' app



class Agent_Policy(models.Model):
    PolicyNo = models.AutoField(primary_key=True)
    agent=models.ForeignKey(AgentRegistration,on_delete=models.CASCADE,null=True)
    policy=models.ForeignKey(Policies,on_delete=models.CASCADE,null=True)
    FinancialYear = models.IntegerField(null=False)
    Total_Policies = models.IntegerField(null=False)
    ModDate = models.DateField(default=now, null=False)

    def __str__(self):
        return f"PolicyNo: {self.PolicyNo}, Agent: {self.agent_id}, FinancialYear: {self.FinancialYear}"
