from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_item, name='add_item'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('item/<int:item_id>/edit/', views.edit_item),
    path('item/<int:item_id>/delete/', views.delete_item),
]