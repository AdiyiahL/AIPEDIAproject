from django.urls import path
from . import views

app_name = 'content'
urlpatterns = [
    path('contentlevel/', views.contentlevel, name='contentlevel'),
    path('add/content/', views.addContent, name='addContent'),
    path('delete/contentlevel/', views.delete_contentlevel, name='delete_contentlevel' ),
    path('edit/contentlevel/', views.edit_contentlevel, name='edit_contentlevel'),
    path('Spacy/', views.spacy, name='spacy'),
    path('content_list/',views.content_list, name='content_list'),
    path('all_read_list/',views.all_read_list, name='all_read_list'),
    path('all_content/',views.all_content, name='all_content'),
    path('play_list/',views.play_list,name='play_list'),
    path('homePage/', views.homePage, name = 'homePage'),
    path('vuetest/', views.vuetest, name='vuetest')
    # path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    # path('change_password/', views.change_password, name='change_password'),
    # path('subscribe/<int:pk>/', views.SubscribeView.as_view(), name='subscribe'),
    # path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    # path('<int:pk>/collect_videos/', views.CollectListView.as_view(), name='collect_videos'),
    # path('<int:pk>/like_videos/', views.LikeListView.as_view(), name='like_videos'),
]