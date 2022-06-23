from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('all/', views.AllTaskListView.as_view(), name='all_task_list'),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name='task_update'),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('<int:pk>/completed/', views.mark_completed, name='mark_completed'),
]
