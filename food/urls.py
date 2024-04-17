from django.urls import path
from . import views
from .views import PlacesListView, PlaceDetailView, AddCommentView, UpdateCommentView, DeleteCommentView
app_name = 'food'
urlpatterns = [
    path('', PlacesListView.as_view(), name='index'),
    path('category/<int:id>/', views.category, name='category'),
    path('detail/<int:id>/', PlaceDetailView.as_view(), name='detail'),
    path('<int:id>/comment', AddCommentView.as_view(), name='add_comment'),
    path('comment_update/', UpdateCommentView.as_view(), name='update_comment'),
    path('comment_delete/<int:id>/', DeleteCommentView.as_view(), name='delete_comment'),
]