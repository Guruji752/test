from django.urls import path
from . import views
urlpatterns=[
            path('',views.index,name='home'),
            path('aboutus',views.aboutus,name='aboutus'),
            path('contactus',views.contactus,name='contactus'),
            path('create_course',views.createcourse,name='createcourse'),
            path('upload_content',views.uploadcontent,name='upload_content'),
            path('privacy_policy',views.privacypolicy,name='privacy_policy')
]