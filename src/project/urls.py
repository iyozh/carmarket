from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("applications.homepage.urls")),
    path("onboarding/", include("applications.onboarding.urls")),
]
