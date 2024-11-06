from django.urls import path
from . import views

# Pages available to admin to monitor inventory and loans
urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('items/', views.item, name='dashboard-item'),
    path('items/delete/<int:pk>/', views.delete_item, name='dashboard-item-delete'),
    path('items/edit/<int:pk>/', views.edit_item, name='dashboard-item-edit'),
    path('loans/', views.loan, name='dashboard-loan'),
    path('loans/return/<int:pk>/', views.returned, name='dashboard-loan-return')
]
