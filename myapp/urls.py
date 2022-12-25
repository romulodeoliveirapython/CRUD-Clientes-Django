from django.urls import path
from myapp import views


app_name = 'myapp'

urlpatterns = [
    path('', views.ClientesList.as_view(), name = 'list'),
    path('create/', views.ClientesCreate.as_view(), name = 'create'),
    path('update/<int:pk>/', views.ClientesUpdate.as_view(), name = 'update'),
    path('detail/<int:pk>/', views.ClientesDetail.as_view(), name = 'detail'),
    path('delete/<int:pk>/', views.ClientesDelete.as_view(), name = 'delete'),
]
