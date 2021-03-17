from django.urls import path
from . import views
urlpatterns=[
            path('',views.coursehome,name='coursehome'),
            path('<int:id>',views.aboutcourse,name='aboutcourse'),
            #path('razorpay/payment/<int:id>',views.razorpay_getway,name='razorpay_getway'),
            path('success',views.coursehome,name='coursehome'),
            path('payment/success',views.success,name='success'),


           path('search',views.search,name='search'),
           path('make_payment',views.paymentpage,name='payment'),
           path('upload_details',views.paymentconform,name='upload_detail'),
           path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
            path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
            path('cart/item_increment/<int:id>/',
                 views.item_increment, name='item_increment'),
            path('cart/item_decrement/<int:id>/',
                 views.item_decrement, name='item_decrement'),
            path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
            path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

]