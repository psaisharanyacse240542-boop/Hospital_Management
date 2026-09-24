from django.contrib import admin
from django.urls import path
from hospital_app import views
from django.urls import path
from hospital_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('hospitals/', views.hospital_list, name='hospitals'),
    path('book/<int:hospital_id>/', views.book_bed, name='book_bed'),
    path('add-hospital/', views.add_hospital, name='add_hospital'),
    path('logout/', views.logout_view, name='logout'),
    path('appointment/', views.book_appointment, name='book_appointment'),
    path('edit-hospital/<int:id>/', views.edit_hospital, name='edit_hospital'),
    path('delete-hospital/<int:id>/', views.delete_hospital, name='delete_hospital'),
    path('rename-hospital/<int:id>/', views.rename_hospital, name='rename_hospital'),

]

