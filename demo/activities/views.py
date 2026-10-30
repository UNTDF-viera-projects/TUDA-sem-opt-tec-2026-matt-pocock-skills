from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST
from .forms import RegistrationForm
from .models import Registration
from .services import CANCELLATION_WINDOW_HOURS, MESSAGES, can_cancel, cancel_registration, register, with_availability

SUCCESS_RESULTS = {"registered", "cancelled"}

def flash_result(request, result):
    severity = "success" if result in SUCCESS_RESULTS else "warning"
    messages.info(request, MESSAGES[result], extra_tags=f"{result} {severity}")

@login_required
def catalog(request):
    # El GROUP BY de annotate() ignora Meta.ordering; el orden explícito sostiene la agrupación por día.
    activities = list(
        with_availability()
        .filter(is_active=True, starts_at__gt=timezone.now())
        .order_by("starts_at", "pk")
    )
    return render(request, "activities/catalog.html", {"activities": activities})

@login_required
def detail(request, pk):
    activity = get_object_or_404(with_availability(), pk=pk)
    registration = Registration.objects.filter(activity=activity, student=request.user).first()
    now = timezone.now()
    open_for_registration = activity.is_active and activity.starts_at > now and activity.available > 0
    return render(request, "activities/detail.html", {"activity": activity, "registration": registration, "can_register": open_for_registration and registration is None, "can_cancel": can_cancel(registration, now), "cancellation_window_hours": CANCELLATION_WINDOW_HOURS, "form": RegistrationForm()})

@login_required
@require_POST
def enroll(request, pk):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        result = register(student=request.user, activity_id=pk)
        flash_result(request, result)
    return redirect("activity_detail", pk=pk)

@login_required
@require_POST
def cancel(request, pk):
    result = cancel_registration(student=request.user, activity_id=pk)
    flash_result(request, result)
    return redirect("activity_detail", pk=pk)

@login_required
def mine(request):
    now = timezone.now()  # Un solo instante para todas las filas.
    registrations = Registration.objects.filter(student=request.user).select_related("activity")
    rows = [{"registration": registration, "can_cancel": can_cancel(registration, now)} for registration in registrations]
    return render(request, "activities/mine.html", {"rows": rows})
