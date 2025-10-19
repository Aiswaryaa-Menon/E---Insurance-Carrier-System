from django.shortcuts import render,redirect, get_object_or_404
from .forms import agentpolform,AgentBuyPolicyForm
from agent.models import Agent_Policy
from company.models import State, Policy_Commission,Policies
from datetime import datetime
from django.contrib import messages

from login.models import AgentRegistration,CustomerRegistration
from users.forms import BuyPolicyForm
from users.models import CustomerPolicy
from company.models import Policies
from django.db.models import F
import re
# Create your views here.
#agentpolicy
def home1(request):
    policies=Policies.objects.all()
    return render(request, "home1.html", {'policies':policies})

#agents


#AGENT POLICY

def ap(request):
    # Initialize the form and fetch data
    form = agentpolform(request.POST or None)
    apol = Agent_Policy.objects.all()

    # Save form if valid
    if form.is_valid():
        form.save()
        return redirect('ap')  # Redirect to the same page

    # Pass data to the template
    context = {
        'form': form,
        'apol': apol,
    }
    return render(request, "ap.html", context)

def editap(request,PolicyNo):
    context = {}
    obj = get_object_or_404(Agent_Policy, PolicyNo=PolicyNo)
    form = agentpolform(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('ap')
    context ['form'] = form
    return render(request,'editap.html',context)

def deleteap(request,PolicyNo):
    context = {}
    obj = get_object_or_404(Agent_Policy,PolicyNo = PolicyNo)
    obj.delete()
    return redirect('ap')


#agentdashboard
def agent_dashboard(request):
    agent_id=request.session.get('Agent_id')
    agent=get_object_or_404(AgentRegistration, pk=agent_id)
    context={
        'agent':agent,
    }
    return render(request,'agent_dashboard.html',context)

#agentcommission
def view_commission(request):
    agents = AgentRegistration.objects.all()
    full_data = []

    for agent in agents:
        agent_data = {
            'agent_id': agent.Agent_id,
            'agent_name': f"{agent.Agent_Fname} {agent.Agent_Lname}",
            'commissions': []
        }

        agent_policies = Agent_Policy.objects.filter(agent=agent)

        for record in agent_policies:
            commission_info = Policy_Commission.objects.filter(policyid=record.policy).first()

            if commission_info and record.policy.sum_assured:
                try:
                    rate = float(commission_info.Comm_Rate.strip('%'))
                except ValueError:
                    rate = 0

                sum_assured = record.policy.sum_assured
                total_commission = ((rate / 100) * sum_assured) * record.Total_Policies

                agent_data['commissions'].append({
                    'policy': record.policy.PolicyName,
                    'rate': commission_info.Comm_Rate,
                    'sum_assured': sum_assured,
                    'total_policies': record.Total_Policies,
                    'total_commission': round(total_commission, 2),
                    'year': record.FinancialYear
                })

        full_data.append(agent_data)

    return render(request, 'view_commission.html', {'full_data': full_data})
#viewpolicy
def view_my_policies(request):
    agent_id = request.session.get("Agent_id")
    if not agent_id:
        return render(request, "error.html", {"msg": "Agent not logged in."})

    agent_policies = Agent_Policy.objects.filter(agent__Agent_id=agent_id).select_related('policy')
    policy_data = []

    for ap in agent_policies:
        commission_entry = Policy_Commission.objects.filter(policyid=ap.policy).first()

        if commission_entry:
            match = re.search(r"(\d+(\.\d+)?)", commission_entry.Comm_Rate)
            commission_rate = float(match.group(1)) if match else 0.0
        else:
            commission_rate = 0.0

        customers = CustomerPolicy.objects.filter(policy_id=ap.policy, agent__Agent_id=agent_id).select_related('customer_id')
        customer_names = [c.customer_id.customer_name for c in customers]

        sum_assured = getattr(ap.policy, 'sum_assured', 0) or 0
        total_commission = round((commission_rate / 100) * sum_assured * ap.Total_Policies, 2)

        policy_data.append({
            'policy_name': ap.policy.PolicyName,
            'financial_year': ap.FinancialYear,
            'total_policies': ap.Total_Policies,
            'commission_rate': f"{commission_rate}%",
            'total_commission': total_commission,
            'customer_names': customer_names
        })

    return render(request, "view_my_policies.html", {'policy_data': policy_data})
#dashboard
def agent_dashboard(request):
    agent_id = request.session.get("Agent_id")

    if not agent_id:
        return redirect('login_view')

    try:
        agent = AgentRegistration.objects.get(Agent_id=agent_id)
    except AgentRegistration.DoesNotExist:
        agent = None

    return render(request, 'agent_dashboard.html', {
        'agent': agent
    })

#buy policy
def agent_buy_policy(request, policy_id):
    if request.session.get("role_type") != "Agent":
        messages.error(request, "Only agents can access this page.")
        return redirect("login_view")

    agent_id = request.session.get("Agent_id")
    agent = get_object_or_404(AgentRegistration, Agent_id=agent_id)
    policy = get_object_or_404(Policies, Policy_Id=policy_id)

    if request.method == 'POST':
        form = AgentBuyPolicyForm(request.POST, request.FILES)
        if form.is_valid():
            customer_instance = form.cleaned_data['customer_id']

            # 🧠 Check if this customer already has this policy
            existing_policy = CustomerPolicy.objects.filter(customer_id=customer_instance, policy_id=policy).first()
            if existing_policy:
                if existing_policy.premium_mode:
                    messages.info(request, "This customer has already completed premium selection. Upload documents next.")
                    return redirect('upload_documents', policy_id=policy_id)
                else:
                    messages.info(request, "This customer already started this policy. Continue to premium selection.")
                    return redirect('choose_premium_mode', policy_id=policy_id)

            # ✅ Update selected customer with form values
            customer_instance.qualification = form.cleaned_data['qualification']
            customer_instance.occupation = form.cleaned_data['occupation']
            customer_instance.height = form.cleaned_data['height']
            customer_instance.weight = form.cleaned_data['weight']
            customer_instance.physical_status = form.cleaned_data['physical_status']
            customer_instance.health_condition = form.cleaned_data['health_condition']
            customer_instance.business_status = form.cleaned_data['business_status']
            customer_instance.identification_mark = form.cleaned_data['identification_mark']
            customer_instance.identity_proof = form.cleaned_data['identity_proof']
            customer_instance.nominee_name = form.cleaned_data['nominee_name']
            customer_instance.nom_rel = form.cleaned_data['nom_rel']
            customer_instance.payment_mode = form.cleaned_data['payment_mode']
            customer_instance.credit_card_no = form.cleaned_data['credit_card_no']
            customer_instance.photo = form.cleaned_data['photo']
            customer_instance.date = form.cleaned_data['date']
            customer_instance.save()

            # 💼 Assign Policy
            CustomerPolicy.objects.create(
                customer_id=customer_instance,
                policy_id=policy,
                agent=agent
            )

            # 📊 Update Agent Policy Table
            agent_policy, created = Agent_Policy.objects.get_or_create(
                agent=agent,
                policy=policy,
                FinancialYear=datetime.now().year,
                defaults={'Total_Policies': 1, 'ModDate': datetime.now().date()}
            )
            if not created:
                agent_policy.Total_Policies += 1
                agent_policy.ModDate = datetime.now().date()
                agent_policy.save()

            messages.success(request, "Policy registered successfully for the selected customer!")
            return redirect('choose_premium_mode')
    else:
        form = AgentBuyPolicyForm()

    return render(request, 'agent_buy_policy.html', {'form': form, 'policy': policy})


