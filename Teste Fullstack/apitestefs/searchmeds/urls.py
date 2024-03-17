from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("med_profiles", views.MedProfileViewSet, basename="MedProfiles")

urlpatterns = [
    path("medprofilelist/", views.MedProfileListCreate.as_view(), name="medprofile-view-create"),
    path("", include(router.urls))
    
]
