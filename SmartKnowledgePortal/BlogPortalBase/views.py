from django.shortcuts import render

# Create your views here.

def BlogPublicPage(request):
    return render(request=request, template_name="BlogPublicPage.html", context={})