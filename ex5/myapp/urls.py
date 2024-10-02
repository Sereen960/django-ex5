from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path('login/', views.login_view, name='login'),  # URL for the login view
    path('profile/', views.profile_view, name='profile'),  # URL for the profile view
    path('set_session/', views.set_session, name='set_session'),  # Optional, if using session setting function
    path('get_session/', views.get_session, name='get_session'),  # Optional, if using session getting function
    path('set_cookies/', views.set_cookies, name='set_cookies'),  # Optional, if using cookies setting function
    path('get_cookies/', views.get_cookies, name='get_cookies'),  # Optional, if using cookies getting function
]
