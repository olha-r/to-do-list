from django.shortcuts import render, redirect
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
# from django.urls import reverse_lazy
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer


# from django.contrib.auth.views import LoginView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login

from .models import Task
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail view': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
        
    }
    return Response(api_urls)
# class CustomLoginView(LoginView):
#     template_name = 'base/login.html'
#     fields = '__all__'
#     redirect_authenticated_user = True
    
#     def get_success_url(self) -> str:
#         return reverse_lazy('tasks')
    
# class RegisterPage(FormView):
#     template_name = 'base/register.html'
#     form_class = UserCreationForm
#     redirect_authenticated_user = True
#     success_url = reverse_lazy('tasks')
#     def form_valid(self, form):
#         user = form.save()
#         if user is not None:
#             login(self.request, user)
#         return super(RegisterPage, self).form_valid(form)
    
#     def get(self, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect('tasks')
#         return super(RegisterPage, self).get(*args, **kwargs)
        
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item deleted !")

# class TaskList(LoginRequiredMixin,ListView):
#     model = Task
#     context_object_name = 'tasks'
    
#     def get_context_data(self, **kwargs):
#             context = super().get_context_data(**kwargs)
#             context['tasks'] = context['tasks'].filter(user=self.request.user)
#             context['count'] = context['tasks'].filter(complete=False).count()
#             search_input = self.request.GET.get('search-area') or ''
#             if search_input:
#                 context['tasks'] = context['tasks'].filter(title__startswith=search_input)
#             context['search_input'] = search_input
#             return context
        
        
    
# class TaskDetail(LoginRequiredMixin,DetailView):
#     model = Task
#     context_object_name = 'task'
#     template_name = 'base/task.html'
    
# class TaskCreate(LoginRequiredMixin,CreateView):
#     model = Task
#     fields = ['title', 'description', 'complete']
#     success_url = reverse_lazy('tasks')
    
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(TaskCreate, self).form_valid(form)
    
# class TaskUpdate(LoginRequiredMixin,UpdateView):
#     model = Task
#     fields = ['title', 'description', 'complete']
#     success_url = reverse_lazy('tasks')
    
# class TaskDelete(LoginRequiredMixin,DeleteView):
#     model = Task
#     context_object_name='task'
#     success_url = reverse_lazy('tasks')
    

    