from django.contrib.messages.context_processors import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest, Http404, HttpResponseServerError


# Create your views here.
@require_GET
def home(request):
    balance = request.session.get("lk_balance", 0)
    return render(request, 'lk_core/dashboard.html', {"balance": balance})

@require_GET
def healthz(request):
    return render(request, 'lk_core/healthz.html')

@require_GET
def award_amount(request,amount: int):
    if not -1000 <= amount <= 1000:
        return HttpResponseBadRequest('Баланс от 0 до 1000 должен быть')
    request.session["lk_balance"] = request.session.get("lk_balance", 0) + amount
    messages.success(request, f"Начислено {+amount}")
    return redirect("lk_core:dashboard")

@require_POST
def award_plus10(request):
    request.session["lk_balance"] = request.session.get("lk_balance", 0) + 10
    messages.success(request, f"Начислено +10")
    return redirect("lk_core:dashboard")
