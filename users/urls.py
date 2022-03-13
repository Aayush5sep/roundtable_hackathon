from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('loginpage/',views.loginpage),
    path('login/',views.loginn),
    path('newaccnt/',views.signup),
    path('newaccntpage/',views.signuppage),
    path('logout/',views.logot),
    path('dashboard/',views.dashboard)
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)