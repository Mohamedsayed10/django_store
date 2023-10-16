from django.urls import path,include
from .views import ProfileView, ProfileUpdateView, ProfileDeleteView, CreateCustomUser
urlpatterns = [
    
    path('',include('django.contrib.auth.urls')),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    path('register/', CreateCustomUser.as_view(), name='register'),
]
