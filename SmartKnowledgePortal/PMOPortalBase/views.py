from django.shortcuts import render

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
    return render(
        request=request, template_name="OnboardingFIllingsPage.html", context={}
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
            request=request, template_name="PMORepository-boardingpass.html", context={}
        )
