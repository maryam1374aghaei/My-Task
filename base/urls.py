from django.urls import path
from . views import Task_List, Task_Detail, Task_Create, Task_Update, Task_Delete,CustomeLoginView, RegisterPages,TaskReorder
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/',CustomeLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='logout'),name='logout'),
    path('register/', RegisterPages.as_view(),name='register'),
    
    path('',Task_List.as_view(), name='tasks'),
    path('task/<int:pk>/',Task_Detail.as_view(), name='task'),
    path('task-create/', Task_Create.as_view(), name='task-create'),
    path('task-update/<int:pk>/',Task_Update.as_view(), name='task-update'),
    path('tasck-delete/<int:pk>/',Task_Delete.as_view(),name='task-delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
]


