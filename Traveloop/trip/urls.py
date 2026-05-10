from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_trip, name='create_trip'),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='trip/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('profile/', views.profile, name='profile'),

    path('<int:trip_id>/', views.trip_detail, name='trip_detail'),
    path('<int:trip_id>/add-stop/', views.add_stop, name='add_stop'),
    path('stop/<int:stop_id>/add-activity/', views.add_activity, name='add_activity'),
    path('toggle-item/<int:item_id>/', views.toggle_packing_item, name='toggle_packing_item'),

    path('community/', views.community, name='community'),
    path('community/trip/<int:trip_id>/', views.public_trip_detail, name='public_trip_detail'),

    # Password Reset URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='trip/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='trip/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='trip/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='trip/password_reset_complete.html'), name='password_reset_complete'),

]