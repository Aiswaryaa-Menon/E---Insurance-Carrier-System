from django.shortcuts import render\

from django.http import JsonResponse
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.utils import timezone

from .forms import companyform,stateform,DistrictForm,insurancetypeform,claimstatusform,PolicyForm,policyfeatureform,policybenefitsform,policydocumentsform,preform,pcform,polpreform,sumform,newsform,claimform
from .models import CompanyBranches,State,District,Insurance_Type,Claim_Status,Policies, Policy_Features,Policy_Benefits,Policy_Documents,Premium_Mode,Policy_Commission,Policy_Premium,Sum_Assured,News,Claims
from login.models import CustomerRegistration
from users.models import CustomerPolicy,CustPolDocs,PremiumSchedules
from datetime import timedelta


def home(request):
    policies = Policies.objects.all().prefetch_related('features', 'benefits')
    return render(request, "company/companyhome.html", {'policies': policies})

#  COMPANY MODEL INSERT, VIEW, EDIT AND DELETE

def compins(request):
    # Initialize the form and fetch data
    form = companyform(request.POST or None)
    branches = CompanyBranches.objects.all()

    # Save form if valid
    if form.is_valid():
        form.save()
        return redirect('compins')  # Redirect to the same page

    # Pass data to the template
    context = {
        'form': form,
        'branches': branches,
    }
    return render(request, "compins.html", context)

def editcompany(request,Branch_Id):
    context = {}
    obj = get_object_or_404(CompanyBranches, Branch_Id=Branch_Id)
    form = companyform(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('compins')
    context ['form'] = form
    return render(request,'comp_edit.html',context)

def deletecompany(request,Branch_Id):
    context = {}
    obj = get_object_or_404(CompanyBranches,Branch_Id = Branch_Id)
    obj.delete()
    return redirect('compins')

#state
def stateins(request):
    form = stateform(request.POST or None)
    stat = State.objects.all()
    if form.is_valid():
        form.save()
        return redirect('stateins')
    context = {
         'form' : form,
         'stat' : stat,
        }
    return render(request,'state.html',context)

def stateedit(request,stateid):
    context = {}
    obj = get_object_or_404(State, stateid=stateid)
    form = stateform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('stateins')
    context ['form']=form
    return render(request,'stateedit.html',context)

def statedelete(request,stateid):
    context={}
    obj =get_object_or_404(State, stateid=stateid)
    obj.delete()
    return redirect('stateins')

#district

def district(request):
    form = DistrictForm(request.POST or None)
    dist = District.objects.all()
    if form.is_valid():
        form.save()
        return redirect('district')

    context = {
    'form' : form,
    'dist' : dist,
    }
    return render(request,'district.html',context)


def editdist(request,distid):
    context = {}
    obj = get_object_or_404(District,distid=distid)
    form = DistrictForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('district')
    context['form'] = form
    return render(request,'editdist.html',context)


def deletedist(request,distid):
    context = {}
    obj = get_object_or_404(District,distid=distid)
    obj.delete()
    return redirect('district')

#dependent dropdown view
def get_districts(request, state_id):
    districts = District.objects.filter(state_id=state_id)
    district_list = [{'id': obj.distid, 'name': obj.distname} for obj in districts]
    return JsonResponse({'district_list': district_list})

#insurancetypes
def instype(request):
    form = insurancetypeform(request.POST or None)
    types = Insurance_Type.objects.all()

    if form.is_valid():
        form.save()
        return redirect(instype)

    context = {
        'form' : form,
        'types':types,
    }

    return render(request,'instype.html',context)

def editinstype(request,InsType_Id):
    context = {}
    obj = get_object_or_404(Insurance_Type, InsType_Id = InsType_Id)
    form = insurancetypeform(request.POST or None, instance= obj)
    if form.is_valid():
        form.save()
        return redirect('instype')
    context['form'] = form
    return render(request, 'editins.html',context)

def deleteinstype(request, InsType_Id):
    context = {}
    obj = get_object_or_404(Insurance_Type,InsType_Id= InsType_Id)
    obj.delete()
    return redirect('instype')

#caimstatus
def claimins(request):
    form = claimstatusform(request.POST or None)
    status = Claim_Status.objects.all()
    if form.is_valid():
        form.save()
        return redirect(claimins)
    context = {
        'form' :form,
        'status': status,
    }
    return render(request, 'claim.html',context)

def editclaim(request,CStatusCode):
    context = {}
    obj = get_object_or_404(Claim_Status, CStatusCode=CStatusCode)
    form = claimstatusform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('claimins')
    context['form'] = form
    return render(request,'editclaim.html',context)

def deleteclaim(request,CStatusCode):
    context = {}
    obj = get_object_or_404(Claim_Status, CStatusCode=CStatusCode)
    obj.delete()
    return redirect('claimins')

#policies
def policies(request):
    form = PolicyForm(request.POST or None)
    pol = Policies.objects.all()

    if form.is_valid():
        form.save()

        return redirect('policies')

    context = {
    'form' : form,
    'pol' : pol,
    }
    return render(request,'policy.html',context)

def editpolicy(request,Policy_Id):
    context = {}
    obj = get_object_or_404(Policies,Policy_Id=Policy_Id)
    form = PolicyForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('policies')
    context['form'] = form
    return render(request,'editpolicy.html',context)

def deletepolicy(request,Policy_Id):
    context = {}
    obj = get_object_or_404(Policies,Policy_Id=Policy_Id)
    obj.delete()
    return redirect('policies')

#POLICY FEATURES
def policyfeature(request):
        form = policyfeatureform(request.POST or None)
        polf = Policy_Features.objects.all()
        if form.is_valid():
            form.save()
            return redirect('policyfeature')

        context = {
            'form': form,
            'polf': polf,
        }
        return render(request, 'policyfea.html', context)

def editpf(request, Feature_Id):
        context = {}
        obj = get_object_or_404(Policy_Features, Feature_Id=Feature_Id)
        form = policyfeatureform(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('policyfeature')
        context['form'] = form
        return render(request, 'editpolicyfea.html', context)

def deletepf(request, Feature_Id):
        context = {}
        obj = get_object_or_404(Policy_Features, Feature_Id=Feature_Id)
        obj.delete()
        return redirect('policyfeature')

#POLICY BENEFITS

def policybenefits(request):
    form = policybenefitsform(request.POST or None)
    polb= Policy_Benefits.objects.all()
    if form.is_valid():
        form.save()
        return redirect('policybenefits')

    context = {
        'form': form,
        'polb': polb,
    }
    return render(request, 'policyben.html', context)


def editpb(request, Benefit_id):
    context = {}
    obj = get_object_or_404(Policy_Benefits, Benefit_id=Benefit_id)
    form = policybenefitsform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('policybenefits')
    context['form'] = form
    return render(request, 'editpolicyben.html', context)

def deletepb(request, Benefit_id):
    context = {}
    obj = get_object_or_404(Policy_Benefits, Benefit_id=Benefit_id)
    obj.delete()
    return redirect('policybenefits')

#POLICY DOCUMENTS
def policydocuments(request):
    form = policydocumentsform(request.POST or None)
    pold= Policy_Documents.objects.all()
    if form.is_valid():
        form.save()
        return redirect('policydocuments')

    context = {
        'form': form,
        'pold': pold,
    }
    return render(request, 'policydoc.html', context)


def editpd(request, Docu_Id):
    context = {}
    obj = get_object_or_404(Policy_Documents, Docu_Id=Docu_Id)
    form = policydocumentsform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('policydocuments')
    context['form'] = form
    return render(request, 'editpolicydoc.html', context)

def deletepd(request, Docu_Id):
    context = {}
    obj = get_object_or_404(Policy_Documents, Docu_Id=Docu_Id)
    obj.delete()
    return redirect('policydocuments')

#PREMIUM_MODE
def premode(request):
    form = preform(request.POST or None)
    prem= Premium_Mode.objects.all()
    if form.is_valid():
        form.save()
        return redirect('premode')

    context = {
        'form': form,
        'prem': prem,
    }
    return render(request, 'pre.html', context)


def editpre(request, pre_mode_id):
    context = {}
    obj = get_object_or_404(Premium_Mode, pre_mode_id=pre_mode_id)
    form = preform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('premode')
    context['form'] = form
    return render(request, 'editpre.html', context)

def deletepre(request, pre_mode_id):
    context = {}
    obj = get_object_or_404(Premium_Mode, pre_mode_id=pre_mode_id)
    obj.delete()
    return redirect('premode')

#POLICY COMMISSION
def pc(request):
    form = pcform(request.POST or None)
    polc= Policy_Commission.objects.all()
    if form.is_valid():
        form.save()
        return redirect('pc')

    context = {
        'form': form,
        'polc': polc,
    }
    return render(request, 'pc.html', context)


def editpc(request, PolComId):
    context = {}
    obj = get_object_or_404(Policy_Commission, PolComId=PolComId)
    form = pcform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('pc')
    context['form'] = form
    return render(request, 'editpc.html', context)

def deletepc(request, PolComId):
    context = {}
    obj = get_object_or_404(Policy_Commission, PolComId=PolComId)
    obj.delete()
    return redirect('pc')

#POLICY PREMIUM

def pp(request):
    form = polpreform(request.POST or None)
    polp= Policy_Premium.objects.all()
    if form.is_valid():
        form.save()
        return redirect('pp')

    context = {
        'form': form,
        'polp': polp,
    }
    return render(request, 'pp.html', context)


def editpp(request, pol_pre_id):
    context = {}
    obj = get_object_or_404(Policy_Premium, pol_pre_id=pol_pre_id)
    form = polpreform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('pp')
    context['form'] = form
    return render(request, 'editpp.html', context)

def deletepp(request, pol_pre_id):
    context = {}
    obj = get_object_or_404(Policy_Premium, pol_pre_id=pol_pre_id)
    obj.delete()
    return redirect('pp')

#sumassured

def sa(request):
    form = sumform(request.POST or None)
    suma= Sum_Assured.objects.all()
    if form.is_valid():
        form.save()
        return redirect('sa')

    context = {
        'form': form,
        'suma': suma,
    }
    return render(request, 'sa.html', context)


def editsa(request, sum_assureid):
    context = {}
    obj = get_object_or_404(Sum_Assured, sum_assureid=sum_assureid)
    form = sumform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('sa')
    context['form'] = form
    return render(request, 'editsa.html', context)

def deletesa(request, sum_assureid):
    context = {}
    obj = get_object_or_404(Sum_Assured, sum_assureid=sum_assureid)
    obj.delete()
    return redirect('sa')

#NEWS
def news(request):
    form = newsform(request.POST or None)
    new= News.objects.all()
    if form.is_valid():
        form.save()
        return redirect('news')

    context = {
        'form': form,
        'new': new,
    }
    return render(request, 'news.html', context)


def editnews(request, newsid):
    context = {}
    obj = get_object_or_404(News, newsid=newsid)
    form = newsform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('news')
    context['form'] = form
    return render(request, 'editnews.html', context)

def deletenews(request, newsid):
    context = {}
    obj = get_object_or_404(News, newsid=newsid)
    obj.delete()
    return redirect('news')

#CLAIMS
def claims(request):
    form = claimform(request.POST or None)
    cl= Claims.objects.all()
    if form.is_valid():
        form.save()
        return redirect('claims')

    context = {
        'form': form,
        'cl': cl,
    }
    return render(request, 'claims.html', context)


def editclaims(request, claim_id):
    context = {}
    obj = get_object_or_404(Claims, claim_id=claim_id)
    form = claimform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('claims')
    context['form'] = form
    return render(request, 'editclaims.html', context)

def deleteclaims(request, claim_id):
    context = {}
    obj = get_object_or_404(Claims, claim_id=claim_id)
    obj.delete()
    return redirect('claims')


#TEMPLATE VIEWS
#HOME PAGE

def thome(request):
    return render(request,'company/companyhome.html')

def cabout(request):
    return render(request,'company/companyabout.html')

def cservices(request):
    return render(request,'company/companyservice.html')




def user_logout(request):
    logout(request)
    return redirect('login_view')


#policydetaildisplay
def company_home(request):
    policies = Policies.objects.all().prefetch_related('features', 'benefits')
    return render(request, 'company/companyhome.html', {'policies': policies})


#adminpolicyview
def admin_policy_view(request,policy_id):
        # Get all CustomerPolicy records with this policy_id
    customer_policies = CustomerPolicy.objects.filter(policy_id=policy_id).select_related('customer_id')

    # Extract the related customers
    customers = [cp.customer_id for cp in customer_policies]

    context = {
        'customers': customers,
        'policy_id':policy_id,
    }
    return render(request, 'admin_policy.html', context)

#documentsview
def view_document(request,customer_id,policy_id):
    documents = CustPolDocs.objects.filter(customer_id=customer_id,policy_id=policy_id)

    context={
        'documents':documents,
    }

    return render(request,'view_documents.html',context)

#verify document
def verify_document(request,poldoc_id):
    doc=CustPolDocs.objects.get(poldoc_id=poldoc_id)
    doc.doc_status='verified'
    doc.save()

    try:
        cust_policy = CustomerPolicy.objects.get(
            customer_id=doc.customer_id,
            policy_id=doc.policy_id
        )
        cust_policy.policy_status = 'approved'
        #cust_policy.agent_id=
        cust_policy.save()

        PremiumSchedules.objects.create(
            cpol_id=cust_policy,
            premium_no='1',
            premium_date=cust_policy.reg_date,
            due_date=cust_policy.reg_date + timedelta(days=30),
            pay_status='pending',
            pre_mode_id=cust_policy.premium_mode
        )

    except CustomerPolicy.DoesNotExist:
        messages.warning(request, "Related policy record not found.")


    messages.success(request,"Document and Policies verified successfully")
    return redirect('home')

#CLAIM DETAILS
def view_claim_details(request):
    claims=Claims.objects.select_related('customer_id','policy_id')
    context={'claims':claims}
    return render(request,'view_claim_details.html',context)


#verifydocs
def verify_claim(request, claim_id):
    claim = get_object_or_404(Claims, claim_id=claim_id)

    if request.method == "POST":
        approved_amt = request.POST.get('approval_amt')
        approved_status = get_object_or_404(Claim_Status, CStatus="Approved")

        claim.pay_status = "Paid"
        claim.app_date = timezone.now().date()
        claim.approval_amt = approved_amt if approved_amt else claim.claim_amt
        claim.cstatus_code = approved_status
        claim.save()

        try:

            print("✅ CLAIM SAVED")
            print(f"👤 Customer Username: {claim.customer_id.Login.username}")
            print(f"📧 Customer Email: {claim.customer_id.email_id}")

            subject = 'Your Claim Has Been Approved 🎉'
            message = f"""Dear {claim.customer_id.Login.username},

Your claim of ₹{claim.claim_amt} has been approved for ₹{claim.approval_amt}.
Approval Date: {claim.app_date}

Thank you for using our services."""

            send_mail(
                subject,
                message,
                'noreply@insurance.com',
                [claim.customer_id.email_id],
                fail_silently=False,
            )

            print("📨 EMAIL SENT SUCCESSFULLY")

        except BadHeaderError:
            print("❌ BadHeaderError: Email not sent.")
        except Exception as e:
            print(f"❌ Email sending failed: {e}")

        messages.success(request, "Claim approved and email sent ✅")
        return redirect('view_claim_details')

    return render(request, 'verify_claim.html', {'claim': claim})