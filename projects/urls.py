from django.urls import path
from . import views

urlpatterns =[
    path('', views.project_list, name='project_list'),

    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('task/<int:task_id>/complete/', views.complete_task, name='complete_task'),
]