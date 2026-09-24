from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Hospital, Doctor,Booking
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

def home(request):
    return render(request, "home.html")

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('dashboard')
            else:
                return redirect('home')
    return render(request, "login.html")

# Register view
def register_view(request):
    if request.method == "POST":
        status = request.POST.get("status")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )

                # If Doctor, save extra fields
                if status == "Doctor":
                    speciality = request.POST.get("speciality")
                    bio = request.POST.get("bio")
                    Doctor.objects.create(
                        hospital=None,  # or assign hospital later
                        name=username,
                        specialization=speciality
                    )
                    # You can also store bio in a separate DoctorProfile model if needed

                return redirect("login")
            else:
                return render(request, "register.html", {"error": "Username already exists"})
        else:
            return render(request, "register.html", {"error": "Passwords do not match"})

    return render(request, "register.html")


# Logout view
def logout_view(request):
    logout(request)
    return redirect("login")


def is_admin(user):
    return user.is_superuser

# Dashboard view
@login_required(login_url='login')
@user_passes_test(is_admin, login_url='login')
def dashboard(request):
    hospitals = Hospital.objects.all()
    return render(request, "dashboard.html", {"hospitals": hospitals})

def delete_hospital(request, id):
    hospital = get_object_or_404(Hospital, id=id)
    hospital.delete()
    return redirect('dashboard')

def rename_hospital(request, id):
    hospital = get_object_or_404(Hospital, id=id)
    new_name = request.GET.get('name')
    if new_name:
        hospital.name = new_name
        hospital.save()
    return redirect('dashboard')

def edit_hospital(request, id):
    hospital = get_object_or_404(Hospital, id=id)

    if request.method == "POST":
        hospital.name = request.POST['name']
        hospital.total_beds = request.POST['total_beds']
        hospital.available_beds = request.POST['available_beds']
        hospital.save()
        return redirect('dashboard')

    return render(request, 'edit_hospital.html', {'hospital': hospital})

# Hospital list
def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request, "hospitals.html", {"hospitals": hospitals})

# Book bed
@login_required
def book_bed(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    if hospital.available_beds > 0:
        hospital.available_beds -= 1
        hospital.save()
        Booking.objects.create(user=request.user, hospital=hospital)
        return render(request, "booking.html", {"hospital": hospital, "success": True})
    return render(request, "booking.html", {"hospital": hospital, "success": False})

# Add hospital
@login_required
def add_hospital(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        total_beds = int(request.POST.get("total_beds"))
        available_beds = int(request.POST.get("available_beds"))

        Hospital.objects.create(
            name=name,
            address=address,
            total_beds=total_beds,
            available_beds=available_beds
        )
        return redirect("dashboard")
    return render(request, "add_hospital.html")

# ✅ Book Appointment page
@login_required
def book_appointment(request):
    if request.method == "POST":
        doctor = request.POST.get("doctor")
        department = request.POST.get("department")
        reason = request.POST.get("reason")
        notes = request.POST.get("notes")
        date = request.POST.get("date")
        time = request.POST.get("time")
        # Save booking (optional: link to Booking model)
        Booking.objects.create(
            # or assign hospital if needed
            user=request.user,
            doctor=doctor,
            department=department,
            reason=reason,
            notes=notes,
            appointment_date=date,
            appointment_time=time
        )
        return render(request, "appointment_confirmation.html", {
            "success":True,
            "doctor": doctor,
            "department": department,
            "reason": reason,
            "date": date,
            "time": time
        })

    return render(request, "book_appointment.html")
