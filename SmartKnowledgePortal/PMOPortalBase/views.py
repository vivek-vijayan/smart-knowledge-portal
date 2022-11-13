from django.shortcuts import render

# Create your views here.


def PMOIndexPage(request):
    return render(
        request=request, template_name="PMOPortalBaseIndexPage.html", context={}
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


def BoardingPassPage(request):
    return render(request=request, template_name="BoardingPass.html", context={})


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
