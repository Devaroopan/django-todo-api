from django.contrib import admin
from django.urls import path, include
from todo.views import todo_html


urlpatterns = [
    path('', todo_html, name='todo-html'),
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),
]
