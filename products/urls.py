from django.urls import path
from products import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    #home page
    path('', views.home, name='home'),
    
    #contact us page
    path('contact/', views.contact, name='contact'),

    #cart
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart_detail'),    
    path('cart/<str:slug>/<str:size>', views.addtocart, name='cart'),

    #orders
    path('orders/', views.orders, name='orders'),

    #all products
    path('allproducts/', views.allprod, name='all_prod'),

    #product detail
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

    #user login/lignup 
    path('usersignup/', views.signup, name='signup'),
    path('userlogin/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('updateprofile/<int:user_id>/', views.updateprofile, name='updateprofile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('profile/', views.profile, name='profile'),
    path('validate_payment/', views.validate_payment, name='validate_payment'),
        
    #Error handlers
    path('handler404/', views.handler404),
    path('handler500/', views.handler500),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
