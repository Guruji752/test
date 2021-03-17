from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('pages.urls')),
                  path('blog/', include('blog.urls')),
                  path('accounts/', include('accounts.urls')),
                  
                  path('contacts/', include('contacts.urls')),
                  path('Courses/', include('course.urls')),
                  path('Student/', include('student.urls')),
                  path('Oppertunities/', include('oppertunities.urls')),
                  path('feedback/', include('review.urls')),
                  path('paypal/',include('paypal.standard.ipn.urls')),
                  path('payments/',include('payments.urls')),
            
                  #path('', include('django.contrib.auth.urls')),
                  #path('bloguser/', include('bloguser.urls')),
                  path('tinymce/', include('tinymce.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
