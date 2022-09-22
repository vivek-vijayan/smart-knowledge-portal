from django.shortcuts import render

# Create your views here.

def PortalLandingIndex(request):
    return render(request=request, template_name="LandingBaseIndexPage.html", context={})
