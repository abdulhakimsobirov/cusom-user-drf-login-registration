from django.urls import path
from .views import RegistrationView, UserListView, UserView, LogoutView, ChangePasswordView, ProfileView, LoginUserView


urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/get/', ProfileView.as_view(), name='profile'),
    path('profile/update/',ProfileView.as_view(), name='profile-update'),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path('user/list/', UserListView.as_view(), name='user-list'),
    path("user/<int:pk>/", UserView.as_view(), name="user"),
    path("logout/", LogoutView.as_view(), name="logout"),

]
