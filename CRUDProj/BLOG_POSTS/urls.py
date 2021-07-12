from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='BPOST'),
    path('create/', views.post_create, name='CreatePOST'),
    path('view/<int:pk>', views.post_view, name='ViewPOST'),
    path('update/<int:pk>', views.post_update, name='UpdatePOST'),
    path('delete/<int:pk>', views.post_delete, name='DeletePOST'),
]