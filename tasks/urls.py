from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='task_update'),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/completed/', views.mark_completed, name='mark_completed'),
]
