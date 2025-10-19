from itertools import count

from django.db.transaction import commit
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import customerform, customerpolicyform, customerdocform, prescheduleform, prepayform, compform, \
    BuyPolicyForm, UploadDocumentsForm, PremiumForm, CompReplyForm,EditProfileForm
from .models import Customer, CustomerPolicy, CustPolDocs, PremiumSchedules, PremiumPayment, Complaints
from login.models import CustomerRegistration,AgentRegistration
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone

from company.models import State, Policies, Policy_Documents, Premium_Mode, Policy_Premium, News, Claims, Claim_Status
from login.models import CustomerRegistration
from users.models import CustomerPolicy, CustPolDocs
from company.forms import claimform
from agent.models import Agent_Policy
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.db.models import Count


# Create your views here.
def home2(request):
    context = {}
    return render(request, "home2.html", context)


def cust(request):
    # Initialize the form and fetch data
    form = customerform(request.POST, request.FILES)
    states = State.objects.all()
    cus = Customer.objects.all()

    # Save form if valid
    if form.is_valid():
        form.save()
        return redirect('cust')  # Redirect to the same page

    # Pass data to the template
    context = {
        'form': form,
        'cus': cus,
        'states': states,
    }
    return render(request, "cust.html", context)


def editcust(request, customer_id):
    context = {}
    obj = get_object_or_404(Customer, customer_id=customer_id)
    form = customerform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('cust')
    context['form'] = form
    return render(request, 'editcust.html', context)


def deletecust(request, customer_id):
    context = {}
    obj = get_object_or_404(Customer, customer_id=customer_id)
    obj.delete()
    return redirect('cust')


# customerpolicy
def cpol(request):
    # Initialize the form and fetch data
    form = customerpolicyform(request.POST or None)
    cusp = CustomerPolicy.objects.all()

    # Save form if valid
    if form.is_valid():
        form.save()
        return redirect('cpol')  # Redirect to the same page

    # Pass data to the template
    context = {
        'form': form,
        'cusp': cusp,
    }
    return render(request, "cpol.html", context)


def editcpol(request, cpol_id):
    context = {}
    obj = get_object_or_404(CustomerPolicy, cpol_id=cpol_id)
    form = customerpolicyform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('cpol')
    context['form'] = form
    return render(request, 'editcpol.html', context)


def deletecpol(request, cpol_id):
    context = {}
    obj = get_object_or_404(CustomerPolicy, cpol_id=cpol_id)
    obj.delete()
    return redirect('cpol')


# customer documents

def cdoc(request):
    # Initialize the form and fetch data
    form = customerdocform(request.POST, request.FILES)
    cusd = CustPolDocs.objects.all()

    # Save form if valid
    if form.is_valid():
        form.save()
        return redirect('cdoc')  # Redirect to the same page

    # Pass data to the template
    context = {
        'form': form,
        'cusd': cusd,
    }
    return render(request, "cdoc.html", context)


def editcdoc(request, poldoc_id):
    context = {}
    obj = get_object_or_404(CustPolDocs, poldoc_id=poldoc_id)
    form = customerdocform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('cdoc')
    context['form'] = form
    return render(request, 'editcdoc.html', context)


def deletecdoc(request, poldoc_id):
    context = {}
    obj = get_object_or_404(CustPolDocs, poldoc_id=poldoc_id)
    obj.delete()
    return redirect('cdoc')


# PREMIUM SCHEDULES

def pres(request):
    # Initialize the form and fetch data
    form = prescheduleform(request.POST or None)
    ps = PremiumSchedules.objects.all()

    # Save form if valid
    if form.is_valid():
        form.save()
        return redirect('pres')  # Redirect to the same page

    # Pass data to the template
    context = {
        'form': form,
        'ps': ps,
    }
    return render(request, "ps.html", context)


def editpres(request, schedule_id):
    context = {}
    obj = get_object_or_404(PremiumSchedules, schedule_id=schedule_id)
    form = prescheduleform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('pres')
    context['form'] = form
    return render(request, 'editps.html', context)


def deletepres(request, schedule_id):
    context = {}
    obj = get_object_or_404(PremiumSchedules, schedule_id=schedule_id)
    obj.delete()
    return redirect('pres')


# PREMIUM PAYMENT

def pm(request):
    # Initialize the form and fetch data
    form = prepayform(request.POST or None)
    prem = PremiumPayment.objects.all()

    # Save form if valid
    if form.is_valid():
        form.save()
        return redirect('pm')  # Redirect to the same page

    # Pass data to the template
    context = {
        'form': form,
        'prem': prem,
    }
    return render(request, "pm.html", context)


def editpm(request, payment_id):
    context = {}
    obj = get_object_or_404(PremiumPayment, payment_id=payment_id)
    form = prepayform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('pm')
    context['form'] = form
    return render(request, 'editpm.html', context)


def deletepm(request, payment_id):
    context = {}
    obj = get_object_or_404(PremiumPayment, payment_id=payment_id)
    obj.delete()
    return redirect('pm')


# COMPLAINTS

def comp(request):
    # Initialize the form and fetch data
    form = compform(request.POST or None)
    cm = Complaints.objects.all()

    # Save form if valid
    if form.is_valid():
        form.save()
        return redirect('comp')  # Redirect to the same page

    # Pass data to the template
    context = {
        'form': form,
        'cm': cm,
    }
    return render(request, "comp.html", context)


def editcomp(request, comp_id):
    context = {}
    complaint = get_object_or_404(Complaints, comp_id=comp_id)
    form = CompReplyForm(request.POST or None, instance=complaint)
    if form.is_valid():
        form.save()
        return redirect('comp')

    return render(request, 'editcomp.html', {'form': form, 'complaint': complaint})


def deletecomp(request, comp_id):
    context = {}
    obj = get_object_or_404(Complaints, comp_id=comp_id)
    obj.delete()
    return redirect('comp')


# POLICYANDFEATURESDISPLAY
def user_home(request):
    policies = Policies.objects.all().prefetch_related('features', 'benefits')
    return render(request, 'home2.html', {'policies': policies})


# readmore
def policy_detail(request, policy_id):
    # Get the policy by its ID
    policy = get_object_or_404(Policies, pk=policy_id)
    features = policy.features.all()  # Get all features related to this policy
    benefits = policy.benefits.all()  # Get all benefits related to this policy

    return render(request, 'company/policy_detail.html', {
        'policy': policy,
        'features': features,
        'benefits': benefits
    })


# buypolicy


def buy_policy(request, policy_id):
    customer_id = request.session.get('Customer_id')

    if not customer_id:
        messages.error(request, "You must be logged in as a customer to buy a policy.")
        return redirect('login_view')

    try:
        customer_instance = CustomerRegistration.objects.get(customer_id=customer_id)
        policy_instance = Policies.objects.get(Policy_Id=policy_id)
    except CustomerRegistration.DoesNotExist:
        messages.error(request, "Customer not found.")
        return redirect('some_error_page')
    except Policies.DoesNotExist:
        messages.error(request, "Policy not found.")
        return redirect('user_home')

    existing_policy = CustomerPolicy.objects.filter(customer_id=customer_instance, policy_id=policy_instance).first()
    if existing_policy:
        if existing_policy.premium_mode:
            messages.info(request, "You’ve already filled the details. Please upload the documents.")
            return redirect('upload_documents', policy_id=policy_id)
        else:
            messages.info(request, "You've already started the process. Please select Premium Mode.")
            return redirect('choose_premium_mode', policy_id=policy_id)

    if request.method == 'POST':
        form = BuyPolicyForm(request.POST, request.FILES)
        if form.is_valid():
            # premium_mode = request.POST.get('pre_mode')
            customer_instance.qualification = form.cleaned_data.get('qualification', customer_instance.qualification)
            customer_instance.occupation = form.cleaned_data.get('occupation', customer_instance.occupation)
            customer_instance.height = form.cleaned_data.get('height', customer_instance.height)
            customer_instance.weight = form.cleaned_data.get('weight', customer_instance.weight)
            customer_instance.physical_status = form.cleaned_data.get('physical_status',
                                                                      customer_instance.physical_status)
            customer_instance.health_condition = form.cleaned_data.get('health_condition',
                                                                       customer_instance.health_condition)
            customer_instance.business_status = form.cleaned_data.get('business_status',
                                                                      customer_instance.business_status)
            customer_instance.identification_mark = form.cleaned_data.get('identification_mark',
                                                                          customer_instance.identification_mark)
            customer_instance.identity_proof = form.cleaned_data.get('identity_proof', customer_instance.identity_proof)
            customer_instance.nominee_name = form.cleaned_data.get('nominee_name', customer_instance.nominee_name)
            customer_instance.nom_rel = form.cleaned_data.get('nom_rel', customer_instance.nom_rel)
            customer_instance.payment_mode = form.cleaned_data.get('payment_mode', customer_instance.payment_mode)
            customer_instance.credit_card_no = form.cleaned_data.get('credit_card_no', customer_instance.credit_card_no)
            customer_instance.photo = form.cleaned_data.get('photo', customer_instance.photo)
            customer_instance.date = form.cleaned_data.get('date', customer_instance.date)
            customer_instance.save()

            agent = AgentRegistration.objects.filter(distid=customer_instance.distid).annotate(num_assigned=Count('customerpolicy')).order_by('num_assigned').first()
            if not agent:
                messages.error(request,'No agents available for your district')
                return redirect('user_home')


            CustomerPolicy.objects.create(
                customer_id=customer_instance,
                policy_id=policy_instance,
                agent=agent,
            )

            agent_policy,created=Agent_Policy.objects.get_or_create(
                agent=agent,
                policy=policy_instance,
                FinancialYear=datetime.now().year,
                defaults={'Total_Policies':1,'ModDate':datetime.now().date()}
            )
            if not created:
                agent_policy.Total_Policies +=1
                agent_policy.ModDate=datetime.now().date()
                agent_policy.save()

            messages.success(request, "Please select Premium Mode!")
            return redirect('choose_premium_mode', policy_id=policy_id)
    else:
        form = BuyPolicyForm()

    context = {
        'form': form,
        'customer_id': customer_id,
        'policy_id': policy_id,
    }
    return render(request, 'buy_policy.html', context)


def upload_documents(request, policy_id):
    customer_id = request.session.get('Customer_id')

    try:
        customer_instance = CustomerRegistration.objects.get(customer_id=customer_id)
        policy_instance = Policies.objects.get(Policy_Id=policy_id)
    except (CustomerRegistration.DoesNotExist, Policies.DoesNotExist):
        messages.error(request, "Invalid customer or policy.")
        return redirect('login_view')

    document_types = Policy_Documents.objects.filter(policyid=policy_instance)

    if request.method == 'POST':
        form = UploadDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            docu = request.POST.get('Docu_Id')
            # print("DOCU_ID from form:", docu)

            CustPolDocs.objects.create(
                customer_id=customer_instance,
                policy_id=policy_instance,
                docu_id_id=docu,
                documents=form.cleaned_data['documents'],
            )
            return redirect('success')
    else:
        form = UploadDocumentsForm()

    return render(request, 'uploaddoc.html', {
        'form': form,
        'policy_id': policy_id,
        'document_types': document_types
    })


def success(request):
    return render(request, 'success.html')


# selectpremiummmode
def choose_premium_mode(request, policy_id):
    customer_id = request.session.get('Customer_id')

    if not customer_id:
        messages.error(request, "Login required")
        return redirect('login_view')

    policy = get_object_or_404(Policies, Policy_Id=policy_id)

    try:
        customer = CustomerRegistration.objects.get(customer_id=customer_id)
        existing_policy = CustomerPolicy.objects.filter(customer_id=customer, policy_id=policy).first()

        if not existing_policy:
            messages.error(request, "Policy process not started. Please fill your details first.")
            return redirect('buy_policy', policy_id=policy_id)

        if existing_policy.premium_mode:
            messages.info(request, "You've already selected this policy and premium mode. Please upload documents.")
            return redirect('upload_documents', policy_id=policy_id)

    except CustomerRegistration.DoesNotExist:
        messages.error(request, "Customer not found.")
        return redirect('user_home')

    if request.method == 'POST':
        selected_pol_pre_id = request.POST.get('pol_pre_id')
        try:
            policy_premium = Policy_Premium.objects.get(pol_pre_id=selected_pol_pre_id)

            existing_policy.premium_mode = policy_premium.premode
            existing_policy.premium_amt = policy_premium.pol_Premium
            existing_policy.save()

            return redirect('upload_documents', policy_id=policy_id)

        except Policy_Premium.DoesNotExist:
            messages.error(request, "Selected premium option not found.")
            return redirect('choose_premium_mode', policy_id=policy_id)

    premium_options = Policy_Premium.objects.filter(policyid=policy)

    return render(request, 'choose_premium_mode.html', {
        'premium_options': premium_options,
        'policy': policy,
    })


# premiumpaymentfirststep
def premium_pay(request):
    if request.method == 'POST':
        form = PremiumForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email_id']
            phone = form.cleaned_data['phone']
            dob = form.cleaned_data['dob']

            try:
                customer = CustomerRegistration.objects.get(email_id=email, phone=phone, dob=dob)
                customer_policies = CustomerPolicy.objects.filter(customer_id=customer)

                if not customer_policies.exists():
                    messages.warning(request, "No policies Found For This Customer")
                    return redirect('premium_pay')
                else:
                    return redirect('view_schedule', customer_id=customer.customer_id)
            except CustomerRegistration.DoesNotExist:
                messages.error(request, "No customer found")
                return redirect('premium_pay')
    else:
        form = PremiumForm()
        return render(request, 'premium_pay.html', {'form': form})


# viewpremiumscheduledetails
def view_schedule(request, customer_id):
    try:
        customer = CustomerRegistration.objects.get(customer_id=customer_id)
        customer_policies = CustomerPolicy.objects.filter(customer_id=customer)
        schedules = PremiumSchedules.objects.filter(
            cpol_id__in=customer_policies,
            due_date__gte=date.today(),
            pay_status='pending'
        )
        all_premiums = Policy_Premium.objects.all()

        for schedule in schedules:
            cp = schedule.cpol_id
            match = all_premiums.filter(policyid=cp.policy_id, premode=cp.premium_mode).first()
            schedule.premium_amount = match.pol_Premium if match else "N/A"

        return render(request, 'premium_schedule.html', {
            'customer': customer,
            'schedules': schedules,

        })
    except CustomerRegistration.DoesNotExist:
        messages.error(request, "Customer not found.")
        return redirect('premium_pay')


# makepayment


def make_payment(request):
    customer_id = request.session.get('Customer_id')
    customer = CustomerRegistration.objects.get(customer_id=customer_id)

    # 1. Get the latest pending premium schedule
    schedule = PremiumSchedules.objects.filter(
        cpol_id__customer_id=customer,
        pay_status='pending',
        due_date__gte=date.today()
    ).select_related('cpol_id').order_by('due_date').first()

    premium_amount = 0
    cust_policy = None

    if schedule:
        cust_policy = schedule.cpol_id
        premium = Policy_Premium.objects.filter(
            policyid=cust_policy.policy_id,
            premode=cust_policy.premium_mode
        ).first()

        if premium:
            premium_amount = premium.pol_Premium
        else:
            print("❌ No matching Policy_Premium found for:", cust_policy.policy_id, cust_policy.premium_mode)
    else:
        print("❌ No pending premium schedules found for this customer")
    print(schedule)
    print(schedule.schedule_id if schedule else "No schedule or schedule_id")
    return render(request, 'make_payment.html', {
        'premium_amount': premium_amount,
        'customer': customer,
        'cust_policy': cust_policy,
        'schedule': schedule,
    })


# sfterpayment
def pay_success(request, schedule_id):
    try:
        schedule = PremiumSchedules.objects.get(schedule_id=schedule_id)

        # Check if this premium is still pending
        if schedule.pay_status == 'pending':
            # Step 1: Mark this schedule as paid
            schedule.pay_status = 'paid'
            schedule.save()

            # Step 2: Fetch customer policy and premium info
            cust_policy = schedule.cpol_id
            premium = Policy_Premium.objects.get(
                policyid=cust_policy.policy_id,
                premode=cust_policy.premium_mode
            )

            # Step 3: Determine payment date
            payment = PremiumPayment.objects.filter(schedule_id=schedule).order_by('-pay_date').first()
            pay_date = payment.pay_date if payment else date.today()

            # Step 4: Calculate next premium date and due date
            premium_mode = cust_policy.premium_mode.pre_mode.lower()
            if premium_mode == 'quarterly':
                next_premium_date = pay_date + relativedelta(months=3)
            elif premium_mode == 'half-yearly':
                next_premium_date = pay_date + relativedelta(months=6)
            elif premium_mode == 'yearly':
                next_premium_date = pay_date + relativedelta(months=12)
            else:
                next_premium_date = pay_date  # fallback

            due_date = next_premium_date + relativedelta(months=1)

            # Step 5: Create the next premium schedule
            next_premium_no = int(schedule.premium_no or 1) + 1
            PremiumSchedules.objects.create(
                cpol_id=cust_policy,
                premium_no=str(next_premium_no),
                premium_date=next_premium_date,
                due_date=due_date,
                pay_status='pending',
                pre_mode_id=schedule.pre_mode_id
            )

            # Step 6: Record payment
            PremiumPayment.objects.create(
                schedule_id=schedule,
                pay_date=pay_date,
                premium_amt=premium.pol_Premium,
                due_amt=0,
                total_amt=premium.pol_Premium
            )

            messages.success(request, "You Successfully Completed The Transaction")
            return redirect('user_home')

        else:
            messages.info(request, "The Amount Is Already Paid")
            return redirect('make_payment')

    except PremiumSchedules.DoesNotExist:
        messages.error(request, "Couldn't find the valid payment schedule to update")
        return redirect('user_home')


# fillcomplaints
def complaint(request):
    if request.method == 'POST':
        form = compform(request.POST)
        if form.is_valid():
            complaints = form.save(commit=False)
            try:

                customer_id = request.session.get("Customer_id")
                if customer_id:
                    customer_instance = CustomerRegistration.objects.get(pk=customer_id)
                    complaints.customer_id = customer_instance
            except CustomerRegistration.DoesNotExist:
                messages.error(request, "Customer profile not found for this user. Please complete registration.")
                return redirect('login_view')
            except CustomerRegistration.MultipleObjectsReturned:
                messages.error(request, "Multiple customer profiles found for this user. Please contact support.")
                return redirect('user_home')
            complaints.comp_date = date.today()
            complaints.save()
            messages.success(request, "Your Complaint has been submitted")
            return redirect('user_home')
    else:
        form = compform()
    return render(request, 'fill_complaint.html', {'form': form})


# news
def seenews(request):
    news_items = News.objects.filter(status='published').order_by('-post_date')
    return render(request, 'seenews.html', {'news_items': news_items})


# viewnews
def news_detail(request, newsid):
    news = get_object_or_404(News, newsid=newsid, status='published')
    return render(request, 'news_detail.html', {'news': news})


# filing a claim

from django.core.exceptions import ObjectDoesNotExist


def file_claim(request):
    if request.method == 'POST':
        form = claimform(request.POST, request.FILES)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.policy_id = Policies.objects.get(PolicyName="Health Insurance")
            claim.cstatus_code = Claim_Status.objects.get(CStatus='New Claim')
            try:

                customer_id = request.session.get("Customer_id")
                if customer_id:
                    customer_instance = CustomerRegistration.objects.get(pk=customer_id)
                    claim.customer_id = customer_instance
            except CustomerRegistration.DoesNotExist:
                messages.error(request, "Customer profile not found for this user. Please complete registration.")
                return redirect('login_view')
            except CustomerRegistration.MultipleObjectsReturned:
                messages.error(request, "Multiple customer profiles found for this user. Please contact support.")
                return redirect('user_home')
            claim.save()
            messages.success(request, "Your Claim Has Been Submitted Successfully")
            return redirect('user_home')
        else:
            print("Form errors:", form.errors)
            print("Form class being used:", form._class_)

    else:
        form = claimform()

    return render(request, 'file_claim.html', {'form': form})


#useraccount
def user_dashboard(request):
    customer_id = request.session.get('Customer_id')
    if not customer_id:
        messages.error(request, "Customer not registered!")
        return redirect('login_view')

    customer = get_object_or_404(CustomerRegistration, pk=customer_id)
    payments = PremiumPayment.objects.filter(
        schedule_id__cpol_id__customer_id=customer_id)
    schedules = PremiumSchedules.objects.filter(cpol_id__customer_id=customer_id)

    return render(request, 'dashboard.html', {
        'customer': customer,
        'payments': payments,
        'schedules': schedules,
    })

#editprofile
def edit_profile(request):
    # Get customer_id from session
    customer_id = request.session.get('Customer_id')

    # Check if user is logged in and has a linked customer
    if not customer_id:
        messages.error(request, "Customer not registered or session expired!")
        return redirect('login_view')

    # Get the customer instance
    customer = get_object_or_404(CustomerRegistration, pk=customer_id)

    # If form submitted
    if request.method == "POST":
        customer.address = request.POST.get('address')
        customer.phone = request.POST.get('phone')
        customer.email_id = request.POST.get('email_id')
        customer.city = request.POST.get('city')
        customer.occupation = request.POST.get('occupation')
        customer.weight = request.POST.get('weight')
        customer.nominee_name = request.POST.get('nominee_name')
        customer.nom_rel = request.POST.get('nom_rel')
        customer.save()

        messages.success(request, "✅ Profile updated successfully.")
        return redirect('edit_profile')  # or redirect to 'user_home'

    # Show form with existing details
    return render(request, 'edit_profile.html', {'customer': customer})
#policies of a specified user
def user_policies(request):
    customer_id = request.session.get('Customer_id')

    if customer_id:
        customer = CustomerRegistration.objects.get(customer_id=customer_id)
        policies = CustomerPolicy.objects.filter(customer_id=customer)

        return render(request, 'user_policies.html', {
            'policies': policies,
            'customer': customer
        })
    else:
        messages.error(request, "Customer session not found. Please log in again.")
        return redirect('login_view')

#claims for a specific user
def my_claims(request):
    customer_id = request.session.get('Customer_id')

    if customer_id:
        claims = Claims.objects.filter(customer_id__customer_id=customer_id)
        return render(request, 'my_claims.html', {'claims': claims})
    else:
        messages.error(request, "Please login again. Session expired.")
        return redirect('login_view')