from django.urls import path
from .views import home, HomeView, todo_detail, list_todos, todo_delete, TodoDeleteView, TodoListView, todo_update, TodoCreateView,TodoUpdateView


urlpatterns = [
#    path('', home, name='home'),
    path('', HomeView.as_view(), name='home'),
#   path('todo_list/', list_todos, name='todo_list'),
    path('list/', TodoListView.as_view(), name='todo_list'),
#  path('create_todo/', todo_create, name='create_todo'),
    path('create/', TodoCreateView.as_view(), name='create_todo'),
    #path('update/<int:id>',todo_update , name='update'),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='update'),
    path('detail/<int:id>', todo_detail, name="detail"),
   # path('delete/<int:id>', todo_delete, name="delete"),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='delete'),


]