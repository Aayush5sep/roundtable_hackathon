from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


# To Be Completed after Google OAuth Verification Completion


urlpatterns = [
    path('',views.links),
    path('addpage/',views.add_page),
    path('add/',views.add_link),
    path('search/',views.search),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)