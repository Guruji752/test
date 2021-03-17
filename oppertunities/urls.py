from django.urls import path
from .import views


urlpatterns = [
    path('Writing/', views.writing, name="Writing"),
    path('Reaserch/', views.research, name="Reaserch"),
    path('Translation/', views.translation, name="Translation"),
    path('HealthCare_LiveSession/', views.healthCare_LiveSession, name="hcls"),
    path('HealthCare_OnlineConseltant/', views.healthCare_OnlineConseltant, name="hcoc"),
    path('healthCare_VideoLesson/', views.healthCare_VideoLesson, name="hcvl"),
    path('Home_care/', views.homeCare, name="homecare"),
    path('apply/', views.apply,name="applynow")
]