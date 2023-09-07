from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("signup/",views.sign_up,name="signup"),
    path("",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("profile/",views.profile,name="profile"),

    # password reset
    path("password_reset/",auth_view.PasswordResetView.as_view(template_name="users/password_reset.html"),name="password_reset"),
    path("password_reset_done/",auth_view.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>",auth_view.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),name="password_reset_confirm"),
    path("password_reset_complete/",auth_view.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),name="password_reset_complete"),
    
]
