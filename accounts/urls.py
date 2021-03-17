from django.urls import path
from .views import register,dashboard, login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth import views as auth_views

urlpatterns=[
            path('login',login,name='login'),
            path('register',register,name='register'),
            path('logout',auth_views.LogoutView.as_view(),name='logout'),
            path('dashboard',dashboard,name='dashboard'),
            path('password-reset/',
		         auth_views.PasswordResetView.as_view(
		             template_name='accounts/password_reset.html'
		         ),
		         name='password_reset'),
		    path('password-reset/done/',
		         auth_views.PasswordResetDoneView.as_view(
		             template_name='accounts/password_reset_done.html'
		         ),
		         name='password_reset_done'),
		    path('password-reset-confirm/<uidb64>/<token>/',
		         auth_views.PasswordResetConfirmView.as_view(
		             template_name='accounts/password_reset_details.html'
		         ),
		         name='password_reset_confirm'),
		    path('password-reset-complete/',
		         auth_views.PasswordResetCompleteView.as_view(
		            template_name='accounts/password_reset_complete.html'
		         ),
		         name='password_reset_complete'),













            
            # path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
            # #path('password/reset', PasswordResetView.as_view(), name='password_reset'),
            # path('password/reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
            # path('password/reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
            # path('password/reset/complete', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
            # path('password/reset', password_reset, name='password_reset'),
            # path('password/reset/done', password_reset_done, name='password_reset_done')
         # path('change_password/',auth_views.PasswordChangeView.as_view(template_name='registration/changepassword.html'))
            #path('change_password/',PasswordsChangeView.as_view(template_name='registration/changepassword.html'))
]