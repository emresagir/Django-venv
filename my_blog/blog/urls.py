from django.urls import include, path
#from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/',AddPostView.as_view(), name='add_post'),
    path('artile/edit/<int:pk>', UpdatePostView.as_view(), name='update-post'),
    path('artile/delete/<int:pk>', DeletePostView.as_view(), name='delete-post'),

]
