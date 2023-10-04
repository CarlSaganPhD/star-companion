from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import UserProfile


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in.
            login(request, user)
            return redirect(
                "login"
            )  # Redirect to a success page, maybe the homepage or a profile page.
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def profile(request):
    return render(request, "accounts/profile.html")


@login_required
def update_level(request):
    if request.method == "POST":
        try:
            new_level = int(request.POST.get("level"))

            profile, created = UserProfile.objects.get_or_create(user=request.user)
            profile.level = new_level
            profile.save()

            return JsonResponse(
                {"success": True, "message": "Level updated successfully."}
            )
        except ValueError:
            return JsonResponse({"success": False, "message": "Invalid level value."})
    return JsonResponse(
        {"success": False, "message": "Method not allowed."}, status=405
    )
