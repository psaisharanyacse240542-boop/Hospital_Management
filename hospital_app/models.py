from django.db import models
from django.contrib.auth.models import User

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    total_beds = models.IntegerField(default=0)
    available_beds = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="doctors")
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.specialization})"
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    appointment_date = models.DateField(blank=True, null=True)
    appointment_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"Booking by {self.user.username} on {self.appointment_date} at {self.appointment_time}"
