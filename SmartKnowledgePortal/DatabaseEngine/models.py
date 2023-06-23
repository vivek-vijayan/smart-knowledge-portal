from django.db import models
from django.contrib.auth.models import User

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
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="project_role_created_by")


class Location(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    location_name = models.CharField(max_length=200, default="Default Location")
    location_short_name = models.CharField(max_length=100, default="LOC")
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="location_created_by")



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
    team_name = models.CharField(max_length=200, default="Team")
    team_leader = models.ForeignKey(TeamLeader, on_delete=models.PROTECT)
    team_description = models.CharField(max_length=200)
    team_da = models.ForeignKey(TeamDA, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="team_created_by")

    def __str__(self) -> str:
        return "Team Name : " + str(self.team_name)


class Module(models.Model):
    module_id = models.BigAutoField(primary_key=True)
    module_name = models.CharField(max_length=200, default="")
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="module_created_by")

class ProjectCode(models.Model):
    project_code_id = models.BigAutoField(primary_key=True)
    project_code = models.CharField(max_length=200, default="")
    start_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="projectcode_created_by")

"""
//////////////////////////////////// Users Profile /////////////////////////////////////////
"""

class Employee(models.Model):
    employee_system_id = models.BigAutoField(primary_key=True)
    employee_short_id = models.CharField(max_length=200)
    corp_id = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    dob = models.DateField(blank=True)
    cg_email = models.EmailField()
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    module = models.ForeignKey(Module, on_delete=models.PROTECT)
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
    backfill_person = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    so_smart = models.CharField(max_length=200, default="")
    pool_of_req = models.CharField(max_length=300)
    so_r2d2 = models.CharField(max_length=200)
    requestor =  models.ForeignKey(User, on_delete=models.PROTECT, related_name="requestor")

    # General
    onboard_date = models.DateTimeField(auto_now=True)
    offboard_date = models.DateTimeField(blank=True)


''' /////////////////////////////////////// BOARDING & MAPPING //////////////////////////////////////////////'''
class Employee_To_Project_Mapping(models.Model):
    e2p_map_id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    project_code = models.ForeignKey(ProjectCode, on_delete=models.PROTECT)
    tag_percent = models.CharField(max_length=200)
    mapped_on = models.DateTimeField(auto_now=True, editable=True)
    mapped_by = models.ForeignKey(User, on_delete=models.PROTECT) 


#class onboard_registration(models.Model):
