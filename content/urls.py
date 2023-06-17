from django.urls import path
from . import views

app_name = 'contents'
urlpatterns = [
    path('contentlevel/', views.contentlevel),
    path('add/content/', views.addContent),
    path('delete/contentlevel/', views.delete_contentlevel),
    path('edit/contentlevel/', views.edit_contentlevel),
    path('Spacy/', views.spacy)
    # path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    # path('change_password/', views.change_password, name='change_password'),
    # path('subscribe/<int:pk>/', views.SubscribeView.as_view(), name='subscribe'),
    # path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    # path('<int:pk>/collect_videos/', views.CollectListView.as_view(), name='collect_videos'),
    # path('<int:pk>/like_videos/', views.LikeListView.as_view(), name='like_videos'),
]