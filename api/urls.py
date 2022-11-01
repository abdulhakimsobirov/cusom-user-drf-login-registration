from django.urls import path
from .views import (ArticleListView, ArticleCreateView, ArticleView, ArticleUpdateView, ArticleDeleteView,
                    BookListView, BookCreateView, BookView, BookUpdateView, BookDeleteView, 
                    DocumentListView, DocumentCreateView, DocumentView, DocumentUpdateView, DocumentDeleteView, 
                    EventListView, EventCreateView, EventView, EventUpdateView, EventDeleteView, 
                    VideoListView, VideoCreateView, VideoView, VideoUpdateView, VideoDeleteView, 
                    GroupUserListView, GroupUserCreateView, GroupUserView, GroupUserUpdateView, GroupUserDeleteView,
                    NewsListView,  NewsCreateView, NewsView, NewsUpdateView, NewsDeleteView,
                    GroupListView, GroupCreateView, GroupView, GroupUpdateView, GroupDeleteView,
                    SmsListView, SmsCreateView, SmsView, SmsUpdateView, SmsDeleteView,
                    CourseListView, CourseCreateView, CourseView, CourseUpdateView, CourseDeleteView)

urlpatterns = [
    path("articles", ArticleListView.as_view()),
    path("articles/create", ArticleCreateView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view()),
    path('articles/<int:pk>/update', ArticleUpdateView.as_view()),
    path('articles/<int:pk>/delete', ArticleDeleteView.as_view()),

    path("books", BookListView.as_view()),
    path("books/create", BookCreateView.as_view()),
    path('books/<int:pk>', BookView.as_view()),
    path('books/<int:pk>/update', BookUpdateView.as_view()),
    path('books/<int:pk>/delete', BookDeleteView.as_view()),

    path("documents", DocumentListView.as_view()),
    path("documents/create", DocumentCreateView.as_view()),
    path('documents/<int:pk>', DocumentView.as_view()),
    path('documents/<int:pk>/update', DocumentUpdateView.as_view()),
    path('documents/<int:pk>/delete', DocumentDeleteView.as_view()),

    path("events", EventListView.as_view()),
    path("events/create", EventCreateView.as_view()),
    path('events/<int:pk>', EventView.as_view()),
    path('events/<int:pk>/update', EventUpdateView.as_view()),
    path('events/<int:pk>/delete', EventDeleteView.as_view()),

    path("videos", VideoListView.as_view()),
    path("videos/create", VideoCreateView.as_view()),
    path('videos/<int:pk>', VideoView.as_view()),
    path('videos/<int:pk>/update', VideoUpdateView.as_view()),
    path('videos/<int:pk>/delete', VideoDeleteView.as_view()),

    path("group_user", GroupUserListView.as_view()),
    path("group_user/create", GroupUserCreateView.as_view()),
    path('group_user/<int:pk>', GroupUserView.as_view()),
    path('group_user/<int:pk>/update', GroupUserUpdateView.as_view()),
    path('group_user/<int:pk>/delete', GroupUserDeleteView.as_view()),

    path("news", NewsListView.as_view()),
    path("news/create", NewsCreateView.as_view()),
    path('news/<int:pk>', NewsView.as_view()),
    path('news/<int:pk>/update', NewsUpdateView.as_view()),
    path('news/<int:pk>/delete', NewsDeleteView.as_view()),

    path("group", GroupListView.as_view()),
    path("group/create", GroupCreateView.as_view()),
    path('group/<int:pk>', GroupView.as_view()),
    path('group/<int:pk>/update', GroupUpdateView.as_view()),
    path('group/<int:pk>/delete', GroupDeleteView.as_view()),

    path("sms", SmsListView.as_view()),
    path("sms/create", SmsCreateView.as_view()),
    path('sms/<int:pk>', SmsView.as_view()),
    path('sms/<int:pk>/update', SmsUpdateView.as_view()),
    path('sms/<int:pk>/delete', SmsDeleteView.as_view()),

    path("course", CourseListView.as_view()),
    path("course/create", CourseCreateView.as_view()),
    path('course/<int:pk>', CourseView.as_view()),
    path('course/<int:pk>/update', CourseUpdateView.as_view()),
    path('course/<int:pk>/delete', CourseDeleteView.as_view()),
    
]