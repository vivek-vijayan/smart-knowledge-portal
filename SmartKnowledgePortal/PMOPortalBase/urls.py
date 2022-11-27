"""SmartKnowledgePortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.PMOIndexPage, name="PMOPortalHomepage"),
    path("onboard/", views.OnboardingFillingPage, name="OnboardingFillingPage"),
    path("offboard/", views.OffboardingInitPage, name="OffboardingInitPage"),
    path("announcement/", views.AnnouncementPage, name="AnnouncementPage"),
    path("boardingstatus/", views.BoardingStatusPage, name="BoardingStatusPage"),
    path("boardingstatus/onboardingpass/", views.OnBoardingPassPage, name="OnBoardingPassPage"),
    path("boardingstatus/offboardingpass/", views.OffBoardingPassPage, name="OffBoardingPassPage"),
    path("tagging-access-new-user/", views.TaggingAndAccessPageForNewUser, name="TaggingAndAccessPageForNewUser"),
    path("success/", views.successpage, name="PMOSuccessPage"),
    path("boardingstatus/request-to-deactivate/", views.RequestToDeactivateAccount, name="RequestToDeactivateAccount"),
    path("pmo-admin/", views.PMOAdminPage, name="PMOAdminPage"),
    path("boardingstatus/pmo-repository/", views.PMORepository, name="PMORepository"),
]
