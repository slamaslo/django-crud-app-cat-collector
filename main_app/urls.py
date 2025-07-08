from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cat_index, name='cat_index'),
    # Function-based view:
    path('cats/<int:cat_id>/', views.cat_detail, name='cat_detail'),
    path('cats/create/', views.CatCreate.as_view(), name='cat_create'),
    # Class-based view:
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
    path('cats/<int:cat_id>/add-feeding/', views.add_feeding, name='add_feeding'),
]