from django.shortcuts import render, redirect

from DatabaseEngine.models import Employee, Location, Grade, Team, Module, ProjectRole
from django.contrib.auth.models import User

# Create your views here.


def PMOIndexPage(request):
    return render(
        request=request, template_name="PMOPortalBaseIndexPage.html", context={}
    )

def PMOAdminPage(request):
    return render(
        request=request, template_name="PMOAdmin.html", context={}
    )



def OnboardingFillingPage(request):
    location = Location.objects.all()
    grade = Grade.objects.all()
    team = Team.objects.all()
    module = Module.objects.all()
    role = ProjectRole.objects.all()
    other_user = User.objects.all()
    return render(
        request=request, template_name="OnboardingFillingsPage.html", context={
            'location' : location,
            'grade': grade,
            'team': team,
            'module': module,
            'role': role,
            'other_user': other_user

        }
    )


def OffboardingInitPage(request):
    return render(request=request, template_name="OffboardingInitPage.html", context={})


def AnnouncementPage(request):
    return render(request=request, template_name="PMOAnnouncement.html", context={})


def BoardingStatusPage(request):
    return render(
        request=request, template_name="BoardingStatusUpdatePage.html", context={}
    )


def OnBoardingPassPage(request):
    return render(request=request, template_name="OnBoardingPass.html", context={})

def OffBoardingPassPage(request):
    return render(request=request, template_name="OffBoardingPass.html", context={})


def TaggingAndAccessPageForNewUser(request):
    return render(
        request=request, template_name="TaggingAndAccessPageNewUser.html", context={}
    )


def successpage(request):
    return render(
        request=request,
        template_name="SuccessPage.html",
        context={"transaction_type": "Onboard initiated"},
    )


def RequestToDeactivateAccount(request):
    return render(
        request=request, template_name="DeactivateAccountRequest.html", context={}
    )

def PMORepository(request, repo_set):
    if(repo_set == 1):
        return render(
            request=request, template_name="PMORepository-boardingpass.html", context={}
        )
    elif(repo_set == 2):
        return render(
            request=request, template_name="PMORepository-userprofile.html", context={}
        )
    else:
        return render(
            request=request, template_name="PMORepository.html", context={}
        )


''' ////////////// PROCESS HANDLER /////////////////'''

def Create_New_Employee_for_OnBoard(request):
    print("VALUE -----------------------------------")
    print(request.POST.get('corp_id', False))
    # Creating a new user in the Smart Portal
    user = User.objects.create_user(request.POST['corp_id'], password='welcome@12345')
    user.first_name = request.POST['firstname']
    user.last_name = request.POST['lastname']
    user.email = request.POST['cg_email']
    user.is_staff = False
    user.is_superuser = False
    user.save()
    # User object has been created

    ''' Creating a new Employee using the user object '''
    try:
        employee = Employee.objects.create(
            employee_short_id = request.POST['emp_id'],
            corp_id = request.POST['corp_id'],
            phone = request.POST['phone'],
            dob = request.POST['dob'],
            cg_email = request.POST['cg_email'],
            team = request.POST['team'],
            module = request.POST['module'],
            location = request.POST['location'],
            supervisor_name = request.POST['supervisor_name'],
            supervisor_email = request.POST['supervisor_email'],
            n_1_name = request.POST['n_1_name'],
            n_1_email = request.POST['n_1_email'],
            asset_type = request.POST['assest'],
            profile_picture = request.FILES['profilepic'],

            # project info
            fte = request.POST['fte'],
            cost_rate = request.POST['cost_rate'],
            spoc = request.POST['spoc'],
            
            # Onboard
            onboard_type = request.POST['onboarding_type'],
            backfill_person = request.POST['backfill_person'],
            so_smart = request.POST['so_smart'],
            pool_of_req = request.POST['pool_req'],
            so_r2d2 = request.POST['so_r2d2'],
            requestor =  request.POST['requestor']
            )
        employee.save()
        redirect('/serco-pmo/tagging-access-new-user/')
    except Exception as e:
        print("Error in creating the employee in the smart portal : " + e)
        
    return redirect('/serco-pmo/tagging-access-new-user')