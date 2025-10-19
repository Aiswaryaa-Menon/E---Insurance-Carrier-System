from django.shortcuts import render

# Create your views here.
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User

from company.models import State, District, CompanyBranches
from users.models import Customer
from .forms import AgentRegistrationForm,CustomerRegistrationForm
from .models import RoleModel,CustomerRegistration,AgentRegistration



def placeholder_view(request):
    return HttpResponse("This is a placeholder.")


def register_agent(request):
    context = {}
    try:
        agent_form = AgentRegistrationForm(request.POST or None)
        if request.POST:
            # Getting form data
            AllocBranch = request.POST.get('AllocBranch')
            Agent_Fname = request.POST.get('Agent_Fname')
            Agent_Lname = request.POST.get('Agent_Lname')
            Address_line1 = request.POST.get('Address_line1')
            Address_line2 = request.POST.get('Address_line2')
            state_id = request.POST.get('stateid')
            dist_id = request.POST.get('distid')
            Contact_no = request.POST.get('Phone')
            Email = request.POST.get('Email_id')
            Qualification = request.POST.get('Qualification')
            DOB = request.POST.get('DOB')
            Gender = request.POST.get('Gender')
            Experience = request.POST.get('Experience')
            Type = request.POST.get('Type')
            Username = request.POST.get('Username')
            Password = request.POST.get('Password')
            ConfirmPassword = request.POST.get('ConfirmPassword')

            # Getting related instances
            state_instance = State.objects.get(stateid=state_id)
            district_instance = District.objects.get(distid=dist_id)
            branch_instance=CompanyBranches.objects.get(Branch_Id=AllocBranch)

            if Password == ConfirmPassword:
                if User.objects.filter(username=Username).exists():
                    messages.info(request, 'This username already exists.')
                    return redirect('register_agent')
                else:
                    # Create User
                    user = User.objects.create_user(username=Username, password=Password)

                    # Create RoleModel entry
                    RoleModel.objects.create(Role='Agent', Login=user)

                    # Create Agent entry
                    AgentRegistration.objects.create(
                        AllocBranch=branch_instance,
                        Agent_Fname=Agent_Fname,
                        Agent_Lname=Agent_Lname,
                        Address_line1=Address_line1,
                        Address_line2=Address_line2,
                        stateid=state_instance,
                        distid=district_instance,
                        Phone=Contact_no,
                        Email_id=Email,
                        Qualification=Qualification,
                        DOB=DOB,
                        Gender=Gender,
                        Experience=Experience,
                        Type=Type,
                        Login=user,
                        Status='Pending'  # Default status
                    )
                    messages.success(request, 'Agent registered successfully!')
                    return redirect('login_view')  # Redirect to login page
            else:
                messages.error(request, "Passwords do not match.")
    except Exception as e:
        error_message = e
        messages.error(request, error_message)


    context['form'] = agent_form
    return render(request, "register_agent.html", context)


def register_customer(request):
    context = {}
    try:
        customer_form = CustomerRegistrationForm(request.POST or None, request.FILES or None)
        states = State.objects.all()

        if request.method == 'POST':
            if customer_form.is_valid():
                Username = customer_form.cleaned_data['Username']
                Password = customer_form.cleaned_data['Password']
                ConfirmPassword = customer_form.cleaned_data['ConfirmPassword']

                if Password == ConfirmPassword:
                    if User.objects.filter(username=Username).exists():
                        messages.info(request, 'This username already exists.')
                        return redirect('register_customer')
                    else:
                        # Create User
                        user = User.objects.create_user(username=Username, password=Password)

                        # Create RoleModel entry
                        RoleModel.objects.create(Role='Customer', Login=user)

                        # Save CustomerRegistration (but don't commit yet)
                        customer = customer_form.save(commit=False)
                        customer.Login = user
                        customer.status = 'Pending'
                        customer.save()

                        messages.success(request, 'Customer registered successfully!')
                        return redirect('login_view')
                else:
                    messages.error(request, "Passwords do not match.")
            else:
                messages.error(request, "Form validation failed.")
    except Exception as e:
        messages.error(request, f"Error: {e}")

    context['form'] = customer_form
    context['states'] = states
    return render(request, "register_customer.html", context)


def login_view(request):
    all_roles = {"Company", "Agent", "Customer"}
    db_roles = set(RoleModel.objects.values_list('Role', flat=True).distinct())
    roles = sorted(all_roles.union(db_roles))
    selected_role = None
    if request.method == "POST":
        usrname = request.POST.get("username")
        psword = request.POST.get("password")
        selected_role = request.POST.get("role")
        user_obj = authenticate(username=usrname, password=psword)

        if user_obj is not None:
              # Logs the user in
            user_id = user_obj.id  # Gets the User ID
            # If the user is an admin
            if user_obj.is_superuser is True:
                request.session["role_type"] = "superuser"
                return HttpResponseRedirect('/company/')  # Redirect to admin panel
            try:
                role_obj = RoleModel.objects.get(Login=user_obj)  # Get user's role
                role_type = role_obj.Role  # Get role type
                request.session["role_type"] = role_type

                if (role_type == 'Agent'):
                    Agent = AgentRegistration.objects.get(Login=user_id)

                    # Store agent session data
                    request.session["Agent_id"] = Agent.Agent_id
                    request.session["Agent_Name"] = f"{Agent.Agent_Fname} {Agent.Agent_Lname}"

                    return HttpResponseRedirect('/agent/')


                elif role_type == 'Customer':
                    customer = CustomerRegistration.objects.get(Login=user_obj)

                    # Store customer session data
                    request.session["Customer_id"] = customer.customer_id
                    request.session["Customer_Name"] = customer.customer_name

                    return redirect('user_home')
  # Redirect customer

                else:
                    messages.error(request, "Unauthorized Role! Please contact support.")
                    return redirect('login')

            except RoleModel.DoesNotExist:
                messages.error(request, "Role not found! Contact support.")
                return redirect('login_view')

            except Agents.DoesNotExist:
                messages.error(request, "Agent data not found! Contact support.")
                return redirect('login_view')

            except Customer.DoesNotExist:
                messages.error(request, "Customer data not found! Contact support.")
                return redirect('login_view')

        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login_view')

    return render(request, 'login.html', {'roles': roles, 'selected_role': selected_role})


