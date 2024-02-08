from django.urls import path
# from .views import TaskList, TaskDetail, TaskCreate,TaskUpdate,TaskDelete, CustomLoginView,RegisterPage
from . import views
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('task-list/', views.taskList, name='task-list'),
    path('task/<str:pk>', views.taskDetail, name='task-detail'),
    path('task-create', views.taskCreate, name='task-create'),
    path('task-update/<str:pk>', views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>', views.taskDelete, name='task-delete'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # path('register/', RegisterPage.as_view(), name='register'),
    
    # path('', TaskList.as_view(), name='tasks'),
    # path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    # path('task-create', TaskCreate.as_view(), name='task-create'),
    # path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    # path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
]
