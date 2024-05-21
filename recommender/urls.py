from django.urls import path
from .views import update_view_history, search, ProductView


urlpatterns = [

    path('update_view_history/', update_view_history, name='update_view_history'),
    path('product/<int:product_id>/', ProductView.as_view(), name='view_product'),
    path('search/', search, name='search'),

]
