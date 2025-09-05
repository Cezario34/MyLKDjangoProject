from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'lk_core/dashboard.html')

def healthz(request):
    return render(request, 'lk_core/healthz.html')