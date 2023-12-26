from django.urls import path
from . import views
urlpatterns = [
     path('login/', views.login, name='login'),
     path('user_list/', views.user_list, name='user_list'),
     path('create_user/', views.create_user, name='create_user'),
     path('delete_user/', views.delete_user, name='delete_user'),
     path('app_list/', views.app_list, name='app_list'),
     path('create_app/', views.create_app, name='create_app'),
     path('delete_app/', views.delete_app, name='delete_app'),
     path('save_app/', views.save_app, name='save_app'),
     path('view_app/', views.view_app, name='view_app'),
     path('view_operator_list/', views.view_operator_list, name='view_operator_list'),
     path('create_task/', views.create_task, name='create_task'),
     path('task_list/', views.task_list, name='task_list'),
     path('edit_operator_list/', views.edit_operator_list, name='edit_operator_list'),
     path('create_operator/', views.create_operator, name='create_operator'),
     path('view_task/', views.view_task, name='view_task'),
     path('delete_task/', views.detete_task, name='detete_task'),
     path('container_list/', views.container_list, name='container_list'),
     path('delete_operator/', views.delete_operator, name='delete_operator'),
     path('server_list/', views.server_list, name='server_list'),
     path('create_server/', views.create_server, name='create_server'),
     path('delete_server/', views.delete_server, name='delete_server'),
     path('get_work_output_img/', views.get_work_output_img, name='get_work_output_img'),
     path('get_task_output_img/', views.get_task_output_img, name='get_task_output_img'),
     path('get_wait_node_by_task/', views.get_wait_node_by_task, name='get_wait_node_by_task'),
]