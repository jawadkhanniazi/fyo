from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('ask/detail/<int:id>',views.detail,name='detail'),
    path('ask/save-comment',views.save_comment,name='save-comment'),
    path('ask/save-upvote',views.save_upvote,name='save-upvote'),
    path('ask/save-downvote',views.save_downvote,name='save-downvote'),
    # User Register
    path('ask/accounts/register/',views.register,name='register'),
    # Profile
    path('ask/accounts/profile/',views.profile,name='profile'),
    # Ask QUestion
    path('ask/ask-question',views.ask_form,name='ask-question'),
    # Tag Page
    path('ask/tag/<str:tag>',views.tag,name='tag'),
    # Tags Page
    path('ask/tags',views.tags,name='tags'),
]