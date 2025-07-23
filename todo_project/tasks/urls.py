from django.urls import path
from . import views, apis

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),

    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # API
    path('api/tasks/', apis.task_list_api),
    path('api/tasks/create/', apis.task_create_api),
    path('api/tasks/<int:pk>/', apis.task_detail_api),
]
