from django.shortcuts import render

# Create your views here.


def SSP_Login(request):
    return render(
        request=request, template_name="AuthenticatorLoginPage.html", context={}
    )
