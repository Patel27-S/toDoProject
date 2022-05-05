from django.urls import path
from .views import home, mainPage, toAddItems, toDeleteItems

urlpatterns = [
    path('main/', home, name='home'),
    path('UsersMainPage/<int:pk>', mainPage, name='mainPage'),
    path('addTodoItem/<int:pk>',toAddItems, name='add_content'),
    path('deleteTodoItem/<int:pk>',toDeleteItems, name='delete_content'),
]