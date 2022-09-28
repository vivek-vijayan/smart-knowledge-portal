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

def AnnouncementPage(request):
    return render(
        request=request, template_name="PMOAnnouncement.html", context={}
    )

def BoardingStatusPage(request):
    return render(
        request=request, template_name="BoardingStatusUpdatePage.html", context={}
    )

def TaggingAndAccessPageForNewUser(request):
    return render(
        request=request, template_name="TaggingAndAccessPageNewUser.html", context={}
    )
