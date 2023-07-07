from django.shortcuts import render, redirect

from DatabaseEngine.models import Employee, Employee_To_Project_Mapping, Location, Grade, ProjectCode, Team, Module, ProjectRole
from django.contrib.auth.models import User

from django.core.files.storage import FileSystemStorage

import datetime
from django.db.models import Q

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
            'location': location,
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

# Boarding control page :


def BoardingStatusPage(request):

    # Waiting list object //////////////////////
    wl_employees = Employee.objects.filter(
        Q(onboard_started=False) or Q(offboard_started=False))

    wl_emp_obj = []
    for _each in wl_employees:
        user = User.objects.get(username=_each.corp_id)
        team = Team.objects.get(team_id=_each.team.team_id)
        location = Location.objects.get(location_id=_each.location.location_id)
        grade = Grade.objects.get(grade_id=_each.grade.grade_id)
        obj = {
            'userid': user.username,
            'name': str(user.first_name) + " " + str(user.last_name),
            'team': team.team_name,
            'location_name': location.location_name,
            'location_image': location.location_fancy,
            'grade': grade.grade_id,
            'profile_image': _each.profile_picture
        }
        wl_emp_obj.append(obj)

    # ///////////////////////////////////////////
    active_employees = Employee.objects.filter(active=True)
    return render(
        request=request, template_name="BoardingStatusUpdatePage.html", context={
            'waiting_list': wl_emp_obj
        }
    )


def OnBoardingPassPage(request):
    return render(request=request, template_name="OnBoardingPass.html", context={})


def OffBoardingPassPage(request):
    return render(request=request, template_name="OffBoardingPass.html", context={})


def TaggingAndAccessPageForNewUser(request, userid):
    user = User.objects.get(username=userid)
    user_firstname = user.first_name
    user_lastname = user.last_name
    employee = Employee.objects.get(corp_id=userid)
    employee_corp = employee.corp_id
    employee_empid = employee.employee_short_id

    available_projects = ProjectCode.objects.filter(active=True)
    assigned_projects = Employee_To_Project_Mapping.objects.filter(
        employee=employee)

    all_codes = []
    for avail in available_projects:
        all_codes.append(avail.project_code_id)

    project_unassigned = []
    project_assigned = []

    for _each_a in assigned_projects:
        try:
            all_codes.remove(_each_a.project_code.project_code_id)
            project_assigned.append({
                'project_code_id': _each_a.project_code.project_code_id,
                'project_code': _each_a.project_code.project_code,
                'project_description': _each_a.project_code.project_description,
                'percent': _each_a.tag_percent
            })
        except:
            print("Error while loading the data for provided data")

    show_assigned = False
    if len(project_assigned) > 0:
        show_assigned = True
    # remaining
    for _each_p in available_projects:
        if (_each_p.project_code_id in all_codes):
            project_unassigned.append({
                'project_code_id': _each_p.project_code_id,
                'project_code': _each_p.project_code,
                'project_description': _each_p.project_description
            })

    show_unassigned = False
    if len(project_unassigned) > 0:
        show_unassigned = True

    return render(
        request=request, template_name="TaggingAndAccessPageNewUser.html", context={
            'firstname': user_firstname,
            'lastname': user_lastname,
            'corp_id': employee_corp,
            'employee_id': employee_empid,
            'assigned_project_code': project_assigned,
            'unassigned_project_code': project_unassigned,
            'show_assigned': show_assigned,
            'show_unassigned': show_unassigned
        }
    )


def Add_Project_Tagging(request):
    try:
        tagging_percent = request.POST['tagging_percent']
        project_code = ProjectCode.objects.get(
            project_code_id=request.POST['tag_project_code_id'])
        user = User.objects.get(username=request.POST['corp_id'])
        emp = Employee.objects.get(emp_obj=user)

        tag_map = Employee_To_Project_Mapping.objects.create(
            employee=emp, project_code=project_code, tag_percent=tagging_percent, mapped_by=request.user)
        tag_map.save()
    except Exception as e:
        print("Failed to map project code" + str(e))
    return redirect('/serco-pmo/tagging-access-new-user/'+str(request.POST['corp_id'])+'/')

def Remove_Project_Tagging(request):
    try:
        project_code = ProjectCode.objects.get(
            project_code_id=request.POST['detag_project_code_id'])
        user = User.objects.get(username=request.POST['corp_id'])
        emp = Employee.objects.get(emp_obj=user)

        entry = Employee_To_Project_Mapping.objects.filter( employee=emp, project_code=project_code).delete()
        entry.save()

    except Exception as e:
        print(e)
    return redirect('/serco-pmo/tagging-access-new-user/'+str(request.POST['corp_id'])+'/')

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
    if (repo_set == 1):
        return render(
            request=request, template_name="PMORepository-boardingpass.html", context={}
        )
    elif (repo_set == 2):
        return render(
            request=request, template_name="PMORepository-userprofile.html", context={}
        )
    else:
        return render(
            request=request, template_name="PMORepository.html", context={}
        )


''' ////////////// PROCESS HANDLER /////////////////'''


def Create_New_Employee_for_OnBoard(request):

    print(request.POST.get('corp_id', False))
    # Creating a new user in the Smart Portal
    user = User.objects.create_user(
        request.POST['corp_id'], password='welcome@12345')
    user.first_name = request.POST['firstname']
    user.last_name = request.POST['lastname']
    user.email = request.POST['cg_email']
    user.is_staff = False
    user.is_superuser = False
    user.save()
    # User object has been created
    upload = request.FILES['profilepic']
    fss = FileSystemStorage()
    file = fss.save(upload.name, upload)

    # Getting the foreign team
    team = Team.objects.get(team_id=request.POST['team'])
    module = Module.objects.get(module_id=request.POST['module'])
    loction = Location.objects.get(location_id=request.POST['location'])
    spoc = User.objects.get(username=request.POST['spoc'])
    replacer = User.objects.get(username=request.POST['backfill_person'])
    requestor = User.objects.get(username=request.POST['requestor'])
    grade = Grade.objects.get(grade_id=request.POST['grade'])

    ''' Creating a new Employee using the user object '''
    try:
        employee = Employee.objects.create(
            employee_short_id=request.POST['emp_id'],
            corp_id=request.POST['corp_id'],
            emp_obj=user,
            phone=request.POST['phone'],
            dob=request.POST['dob'],
            cg_email=request.POST['cg_email'],
            team=team,
            module=module,
            location=loction,
            supervisor_name=request.POST['supervisor_name'],
            supervisor_email=request.POST['supervisor_email'],
            n_1_name=request.POST['n_1_name'],
            n_1_email=request.POST['n_1_email'],
            asset_type=request.POST['asset'],
            profile_picture=file,
            grade=grade,

            # project info
            fte=request.POST['fte'],
            cost_rate=request.POST['cost_rate'],
            spoc=spoc,

            # Onboard
            onboard_type=request.POST['onboarding_type'],
            backfill_person=replacer,
            so_smart=request.POST['so_smart'],
            pool_of_req=request.POST['pool_req'],
            so_r2d2=request.POST['so_r2d2'],
            requestor=requestor,
            offboard_date=datetime.date(9999, 12, 31),
            onboard_date=datetime.date(9999, 12, 31),
            active=False
        )
        employee.save()
        redirect('/serco-pmo/tagging-access-new-user/' +
                 str(user.username) + "/")
    except Exception as e:
        print("Error in creating the employee in the smart portal : " + str(e))

    return redirect('/serco-pmo/tagging-access-new-user/' + str(user.username) + "/")
