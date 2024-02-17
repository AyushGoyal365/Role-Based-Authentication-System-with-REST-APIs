from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import EmployeeViewSet ,register_user, user_login
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView,
)
from rest_framework.authtoken import views

# Create a router object
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

# Define the urlpatterns
urlpatterns = [
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-auth/', views.obtain_auth_token),
    path('verifytoken/',TokenVerifyView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
   
   
]

