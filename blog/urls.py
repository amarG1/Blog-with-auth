from . import views
from django.urls import path
from  django.conf import settings
from django.conf.urls.static import static
from .views import MyView,Create,UpdateView,DeleteView




urlpatterns = [
    path('', views.index, name='home'),
    
    path('postlist/', views.PostList.as_view(), name='post'),
    
    path('new/', Create.as_view(),name='addpost' ),
     path('about/', MyView.as_view()),
    path('postlist/<pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('postlist/<pk>/update', UpdateView.as_view(),name='post_update'),
    path('postlist/<pk>/delete', DeleteView.as_view(),name='post_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)