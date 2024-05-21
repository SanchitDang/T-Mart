from django.urls import path
from admin_panel import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('login/', views.admin_login, name='admin_login'),
    path('webadmin/', views.admin_dashboard, name='admin_dashboard'),
    path('all_users/', views.all_users, name='all_users'),
    path('all_orders/', views.all_orders, name='all_orders'),
    path('all_products/', views.all_products, name='all_products'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_brand/', views.add_brand, name='add_brand'),
    path('add_occassion/', views.add_occassion, name='add_occassion'),
    path('add_color/', views.add_color, name='add_color'),
    path('add_neck/', views.add_neck, name='add_neck'),
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)