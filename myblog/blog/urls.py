from django.urls import path
from . import views



urlpatterns = [

    path('',views.HomeView.as_view(),name='index'),
    path('posts/',views.PostListView.as_view(),name='post_list'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('success/',views.Success.as_view(),name='success'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

]

