from django.urls import path
from .views import (
    MyTokenObtainPairView,
    register_view,
    admin_only,
    list_users,
    update_user,
    delete_user,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', register_view),
    path('admin-only/', admin_only),
    
    path('users/', list_users),          # GET
    path('users/<int:pk>/', update_user),# PUT
    path('users/<int:pk>/delete/', delete_user),  # DELETE
]
