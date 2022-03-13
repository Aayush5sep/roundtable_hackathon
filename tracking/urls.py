from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.tracking),
    path('auth/',views.auth)
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# Rest Project to be Completed after Google Oauth app verification to read gmails