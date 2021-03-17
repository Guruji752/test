from django.urls import path
from . import views
from .views import *

#app_name='blog'
urlpatterns=[
path('process/<int:id>',payment_process,name='process'),
path('done',payment_done,name='done'),
path('canceled',payment_canceled,name='canceled '),
# path('delete_post/<int:pk>',DeletePost.as_view(),name='delete_post')
#path('tag/<slug:tag_slug>/',views.post_list,name='post_list_by_tag'),
#path('<int:post_id>/share/',views.post_share,name='post_share'),
#path('<slug:post>',views.post_details,name='post_details')
]