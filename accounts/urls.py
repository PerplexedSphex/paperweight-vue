from django.urls import path, include

from .views import SignupView


accounts_patterns = [
    path('', include('authtools.urls')),
    path('signup/', SignupView.as_view(), name='signup')
]

urlpatterns = [
    path('accounts/', include(accounts_patterns))
]
