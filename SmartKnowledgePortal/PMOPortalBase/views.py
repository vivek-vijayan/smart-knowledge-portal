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
