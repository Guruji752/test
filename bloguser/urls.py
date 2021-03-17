from  django.urls import path
from .views import BlogRegistration


urlpatterns=[
    path('blog_registration',BlogRegistration.as_view(),name="blog_registration"),
]