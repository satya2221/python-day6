from django.urls import path

from .views import IndexView, DetailView, DeleteView, UpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('todos/<str:id>', DetailView.as_view(), name='detail-view'),
    path('todos/<str:id>/delete/', DeleteView.as_view(), name='delete'),
    path('todos/<str:id>/update/',UpdateView.as_view(), name="update")
]