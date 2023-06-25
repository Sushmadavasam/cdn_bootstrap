from django.shortcuts import render

# Create your views here.
def cdn_bootstrap(request):
    return render(request,'cdn_bootstrap.html')