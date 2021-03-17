from django.urls import path
#from . import views
from .views import HomeView,BlogDetail,AddPost,UpdatePost,DeletePost

#app_name='blog'
urlpatterns=[
path('',HomeView.as_view(),name='bloghome'),
path('detail/<int:pk>',BlogDetail.as_view(),name='blogdetail'),
path('add_post',AddPost.as_view(),name='addpost'),
path('update_post/<int:pk>',UpdatePost.as_view(),name='update_post'),
path('delete_post/<int:pk>',DeletePost.as_view(),name='delete_post')
#path('tag/<slug:tag_slug>/',views.post_list,name='post_list_by_tag'),
#path('<int:post_id>/share/',views.post_share,name='post_share'),
#path('<slug:post>',views.post_details,name='post_details')
]