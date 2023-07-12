from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
"""
Smart Portal Central Database Schema:

Developed : Vivek Vijayan
Recently : 22 -09 -2022

"""

# General Models
class Grade(models.Model):
    grade_id = models.CharField(max_length=200, primary_key=True)
    grade_name = models.CharField(max_length=200, default="Analyst")
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="grade_created_by")

    def __str__(self) -> str:
        return super().__str__()


class ProjectRole(models.Model):
    project_role_id = models.BigAutoField(primary_key=True)
    project_role_name = models.CharField(max_length=200, default="Default Name")
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="project_role_created_by")

    def __str__(self) -> str:
        return str(self.project_role_name)

class Location(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    location_name = models.CharField(max_length=200, default="Default Location")
    location_short_name = models.CharField(max_length=100, default="LOC")
    location_fancy = models.CharField(default="", max_length=500)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="location_created_by")

    def __str__(self) -> str:
        return str(self.location_name)

"""////////////////////////////////// KNOWLEDGE HUB TEAM TABLES ////////////////////////////////////////"""


# Team Leader Model
class TeamLeader(models.Model):
    team_leader_id = models.BigAutoField(primary_key=True)
    team_leader_user = models.ForeignKey(User, on_delete=models.PROTECT)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(blank=True)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="tl_created_by")

    def __str__(self) -> str:
        return "Team Leader : " + str(self.team_leader_user)


# Team Design Authority model
class TeamDA(models.Model):
    team_da_id = models.BigAutoField(primary_key=True)
    team_da_user = models.ForeignKey(User, on_delete=models.PROTECT)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(blank=True)
    active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="da_created_by")

    def __str__(self) -> str:
        return "Team DA : " + str(self.team_da_user)


# Team models
class Team(models.Model):
    team_id = models.BigAutoField(primary_key=True)
    team_name = models.CharField(max_length=4, default="Team")
    team_leader = models.ForeignKey(TeamLeader, on_delete=models.PROTECT)
    team_description = models.CharField(max_length=200)
    team_da = models.ForeignKey(TeamDA, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="team_created_by")

    def __str__(self) -> str:
        return  str(self.team_name)


class Module(models.Model):
    module_id = models.BigAutoField(primary_key=True)
    module_name = models.CharField(max_length=200, default="")
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="module_created_by")

    def __str__(self) -> str:
        return str(self.module_name)

class ProjectCode(models.Model):
    project_code_id = models.BigAutoField(primary_key=True)
    project_code = models.CharField(max_length=200, default="")
    project_description = models.CharField(max_length=200, default="Project Code")
    start_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="projectcode_created_by")
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.project_code)

"""
//////////////////////////////////// Users Profile /////////////////////////////////////////
"""

class Employee(models.Model):
    employee_system_id = models.BigAutoField(primary_key=True)
    employee_short_id = models.CharField(max_length=200)
    corp_id = models.CharField(max_length=200)
    emp_obj = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, related_name="employee", default="")
    phone = models.CharField(max_length=200)
    dob = models.DateField(blank=True)
    cg_email = models.EmailField()
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    module = models.ForeignKey(Module, on_delete=models.PROTECT)
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT, default=1)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    supervisor_name = models.CharField(max_length=200, default="")
    supervisor_email = models.EmailField()
    n_1_name = models.CharField(max_length=200, default="")
    n_1_email = models.EmailField()
    asset_type = models.CharField(max_length=200, default="")
    profile_picture = models.ImageField(upload_to='profile-picture/')

    # project info
    fte = models.CharField(max_length=200, default="")
    cost_rate = models.CharField(max_length=200, default="")
    spoc = models.ForeignKey(User, on_delete=models.PROTECT, related_name="spoc")
    
    # Onboard
    onboard_type = models.CharField(max_length=200)
    backfill_person = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, related_name="backfill")
    so_smart = models.CharField(max_length=200, default="")
    pool_of_req = models.CharField(max_length=300)
    so_r2d2 = models.CharField(max_length=200)
    requestor =  models.ForeignKey(User, on_delete=models.PROTECT, related_name="requestor")

    # General
    onboard_date = models.DateTimeField(auto_now=True)
    offboard_date = models.DateTimeField(blank=True)

    # verfication
    verfied = models.BooleanField(default=False)

    #Active Employee?
    active = models.BooleanField(default=False)
    onboard_started = models.BooleanField(default=False)
    offboard_started = models.BooleanField(default=False)

    def __str__(self):
        return str(self.corp_id) + " - " + str(self.employee_short_id)


class Background_Verification(models.Model):
    verification_id = models.BigAutoField(primary_key=True)
    verification_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    verified_approved_by = models.ForeignKey(User, on_delete=models.PROTECT)
    verified_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.verification_employee


''' /////////////////////////////////////// BOARDING & MAPPING //////////////////////////////////////////////'''
class Employee_To_Project_Mapping(models.Model):
    e2p_map_id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    project_code = models.ForeignKey(ProjectCode, on_delete=models.PROTECT)
    tag_percent = models.CharField(max_length=200)
    mapped_on = models.DateTimeField(auto_now=True, editable=True)
    mapped_by = models.ForeignKey(User, on_delete=models.PROTECT) 


class Onboard_registration(models.Model):
    onboard_reg_id = models.BigAutoField(primary_key=True)
    employee_onboard = models.ForeignKey(Employee, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='onboard_created_by')
    raised_by = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name="onboard_raised_by")
    closed = models.BooleanField(default=False)
    closed_on = models.DateTimeField(default=datetime.date(9999, 12, 31))
    
    
class Onboard_process_timeline(models.Model):
    onboard_process_timeline_id = models.BigAutoField(primary_key=True)
    onboard_reg_no = models.ForeignKey(Onboard_registration, on_delete=models.PROTECT)
    process_name = models.CharField(max_length=200, default="Process")
    process_status = models.CharField(max_length=200, default="Not Started")
    process_description = models.CharField(max_length=200, default="New Process")
    process_owner = models.ForeignKey(User, on_delete=models.PROTECT)
    process_start_date = models.DateTimeField(auto_now=True)
    process_end_date = models.DateTimeField(blank=True)
    active = models.BooleanField(default=True) 
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='onboard_timeline_created_by')

    def __str__(self) -> str:
        return super().__str__()
    
class Onboarding_ticket_relation(models.Model):
    onboard_ticket_relation = models.BigAutoField(primary_key=True)
    ticket_number = models.CharField(max_length=200, default="TICKET")
    ticket_short_desc = models.CharField(max_length=200, default="")
    ticket_long_desc = models.CharField(max_length=500, default="")
    raised_by = models.ForeignKey(User, on_delete=models.PROTECT)
    raised_on = models.DateTimeField(auto_now=True)
    ticket_link = models.URLField(default="#")
    timeline_relation = models.ForeignKey(Onboard_process_timeline, on_delete=models.PROTECT)


'''
////////////////////////////// ACCESS TO PORTAL ///////////////////////////////////////
'''

# Admin level required
class App_Module_Registration(models.Model):
    app_register_id = models.BigAutoField(primary_key=True)
    app_name = models.CharField(max_length=10)
    app_short_name = models.CharField(max_length=5)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return super().__str__()
    
class Access_To_App_Portal(models.Model):
    access_registration_id = models.BigAutoField(primary_key=True)
    access_module = models.ForeignKey(App_Module_Registration, on_delete=models.PROTECT)
    access_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="access_user")
    access_validity_end = models.DateTimeField(default=datetime.date(9999, 12, 31))
    access_provided_on = models.DateTimeField(auto_now=True)
    provided_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="provided_by")

    def __str__(self) -> str:
        return super().__str__()

