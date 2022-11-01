from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import *
from .filters import GroupFilter, SmsFilter
from config.mixins import ListAPIViewResponseMixin, RetrieveAPIViewResponseMixin, CreateAPIViewResponseMixin, \
    UpdateAPIViewResponseMixin, DestroyAPIViewResponseMixin

from .serializers import ArticleSerializer, CoursesSerializer, VideoSerializer, BookSerializer, DocumentSerializer, EventSerializer, GroupUserSerializer, NewSerializer, GroupSerializer, SmsSerializer
# ---------------------------------------------------Article------------------------------------------
class BaseArticleView:
    queryset = Articles.objects.all()
    # permission_classes = [IsAuthenticated]


class ArticleListView(BaseArticleView, ListAPIViewResponseMixin, generics.ListAPIView):
    serializer_class = ArticleSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter]
    # filter_fields = ['content']
    # search_fields = ['name']
    # field = 'name'


class ArticleView(BaseArticleView, RetrieveAPIViewResponseMixin, generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    # field = 'name'


class ArticleCreateView(BaseArticleView, CreateAPIViewResponseMixin, generics.CreateAPIView):
    serializer_class = ArticleSerializer


class ArticleUpdateView(BaseArticleView, UpdateAPIViewResponseMixin, generics.UpdateAPIView):
    serializer_class = ArticleSerializer


class ArticleDeleteView(BaseArticleView, DestroyAPIViewResponseMixin, generics.DestroyAPIView):
    pass


# ---------------------------------------------------Books-----------------------------------------

class BaseBookView:
    queryset = Books.objects.all()
    # permission_classes = [IsAuthenticated]


class BookListView(BaseBookView, ListAPIViewResponseMixin, generics.ListAPIView):
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['content']
    search_fields = ['name']
    field = 'name'


class BookView(BaseBookView, RetrieveAPIViewResponseMixin, generics.RetrieveAPIView):
    serializer_class = BookSerializer
    field = 'name'


class BookCreateView(BaseBookView, CreateAPIViewResponseMixin, generics.CreateAPIView):
    serializer_class = BookSerializer


class BookUpdateView(BaseBookView, UpdateAPIViewResponseMixin, generics.UpdateAPIView):
    serializer_class = BookSerializer


class BookDeleteView(BaseBookView, DestroyAPIViewResponseMixin, generics.DestroyAPIView):
    pass

# -----------------------------------------------------Documents-------------------------------------------------

class BaseDocumentView:
    queryset = Documents.objects.all()
    # permission_classes = [IsAuthenticated]


class DocumentListView(BaseDocumentView, ListAPIViewResponseMixin, generics.ListAPIView):
    serializer_class = DocumentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['content']
    search_fields = ['name']
    field = 'name'


class DocumentView(BaseDocumentView, RetrieveAPIViewResponseMixin, generics.RetrieveAPIView):
    serializer_class = DocumentSerializer
    field = 'name'


class DocumentCreateView(BaseDocumentView, CreateAPIViewResponseMixin, generics.CreateAPIView):
    serializer_class = DocumentSerializer


class DocumentUpdateView(BaseDocumentView, UpdateAPIViewResponseMixin, generics.UpdateAPIView):
    serializer_class = DocumentSerializer


class DocumentDeleteView(BaseDocumentView, DestroyAPIViewResponseMixin, generics.DestroyAPIView):
    pass


# ------------------------------------------------------Events-------------------------------------------------------

class BaseEventView:
    queryset = Events.objects.all()
    # permission_classes = [IsAuthenticated]


class EventListView(BaseEventView, ListAPIViewResponseMixin, generics.ListAPIView):
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['content']
    search_fields = ['name']
    field = 'name'


class EventView(BaseEventView, RetrieveAPIViewResponseMixin, generics.RetrieveAPIView):
    serializer_class = EventSerializer
    field = 'name'


class EventCreateView(BaseEventView, CreateAPIViewResponseMixin, generics.CreateAPIView):
    serializer_class = EventSerializer


class EventUpdateView(BaseEventView, UpdateAPIViewResponseMixin, generics.UpdateAPIView):
    serializer_class = EventSerializer


class EventDeleteView(BaseEventView, DestroyAPIViewResponseMixin, generics.DestroyAPIView):
    pass


# ----------------------------------------------Videos------------------------------------------------


class BaseVideoView:
    queryset = Videos.objects.all()
    # permission_classes = [IsAuthenticated]


class VideoListView(BaseVideoView, ListAPIViewResponseMixin, generics.ListAPIView):
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    
    search_fields = ['name']
    field = 'name'


class VideoView(BaseVideoView, RetrieveAPIViewResponseMixin, generics.RetrieveAPIView):
    serializer_class = VideoSerializer
    field = 'name'


class VideoCreateView(BaseVideoView, CreateAPIViewResponseMixin, generics.CreateAPIView):
    serializer_class = VideoSerializer


class VideoUpdateView(BaseVideoView, UpdateAPIViewResponseMixin, generics.UpdateAPIView):
    serializer_class = VideoSerializer


class VideoDeleteView(BaseVideoView, DestroyAPIViewResponseMixin, generics.DestroyAPIView):
    pass

# --------------------------------------------GroupUser-----------------------------------------------

class BaseGroupUserView:
    queryset = GroupUser.objects.all()
    # permission_classes = [IsAuthenticated]


class GroupUserListView(BaseGroupUserView, ListAPIViewResponseMixin, generics.ListAPIView):
    serializer_class = GroupUserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # filter_fields = ['content']
    # search_fields = ['name']
    # field = 'name'


class GroupUserView(BaseGroupUserView, RetrieveAPIViewResponseMixin, generics.RetrieveAPIView):
    serializer_class = GroupUserSerializer
    # field = 'name'


class GroupUserCreateView(BaseGroupUserView, CreateAPIViewResponseMixin, generics.CreateAPIView):
    serializer_class = GroupUserSerializer


class GroupUserUpdateView(BaseGroupUserView, UpdateAPIViewResponseMixin, generics.UpdateAPIView):
    serializer_class = GroupUserSerializer


class GroupUserDeleteView(BaseGroupUserView, DestroyAPIViewResponseMixin, generics.DestroyAPIView):
    pass


# --------------------------------------------------News-----------------------------------------------
class BaseNewsView:
    queryset = News.objects.all()
    # permission_classes = [IsAuthenticated]


class NewsListView(BaseNewsView, ListAPIViewResponseMixin, generics.ListAPIView):
    serializer_class = NewSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter]
    # filter_fields = ['content']
    # search_fields = ['name']
    # field = 'name'


class NewsView(BaseNewsView, RetrieveAPIViewResponseMixin, generics.RetrieveAPIView):
    serializer_class = NewSerializer
    # field = 'name'


class NewsCreateView(BaseNewsView, CreateAPIViewResponseMixin, generics.CreateAPIView):
    serializer_class = NewSerializer


class NewsUpdateView(BaseNewsView, UpdateAPIViewResponseMixin, generics.UpdateAPIView):
    serializer_class = NewSerializer


class NewsDeleteView(BaseNewsView, DestroyAPIViewResponseMixin, generics.DestroyAPIView):
    pass


# -------------------------------------------Group------------------------------------------

class BaseGroupView:
    queryset = Group.objects.all()
    # permission_classes = [IsAuthenticated]


class GroupListView(BaseGroupView, ListAPIViewResponseMixin, generics.ListAPIView):
    serializer_class = GroupSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = GroupFilter
    field = 'name'


class GroupView(BaseGroupView, RetrieveAPIViewResponseMixin, generics.RetrieveAPIView):
    serializer_class = GroupSerializer
    field = 'name'


class GroupCreateView(BaseGroupView, CreateAPIViewResponseMixin, generics.CreateAPIView):
    serializer_class = GroupSerializer


class GroupUpdateView(BaseGroupView, UpdateAPIViewResponseMixin, generics.UpdateAPIView):
    serializer_class = GroupSerializer


class GroupDeleteView(BaseGroupView, DestroyAPIViewResponseMixin, generics.DestroyAPIView):
    pass

# ----------------------------------------------Sms----------------------------------------
class BaseSmsView:
    queryset = Sms.objects.all()
    # permission_classes = [IsAuthenticated]


class SmsListView(BaseSmsView, ListAPIViewResponseMixin, generics.ListAPIView):
    serializer_class = SmsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = SmsFilter
    field = 'group'


class SmsView(BaseSmsView, RetrieveAPIViewResponseMixin, generics.RetrieveAPIView):
    serializer_class = SmsSerializer
    # field = 'name'


class SmsCreateView(BaseSmsView, CreateAPIViewResponseMixin, generics.CreateAPIView):
    serializer_class = SmsSerializer


class SmsUpdateView(BaseSmsView, UpdateAPIViewResponseMixin, generics.UpdateAPIView):
    serializer_class = SmsSerializer


class SmsDeleteView(BaseSmsView, DestroyAPIViewResponseMixin, generics.DestroyAPIView):
    pass


# ----------------------------------------------Courses--------------------------------------------


class BaseCourseView:
    queryset = Courses.objects.all()
    # permission_classes = [IsAuthenticated]


class CourseListView(BaseCourseView, ListAPIViewResponseMixin, generics.ListAPIView):
    serializer_class = CoursesSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_class = SmsFilter
    # field = 'group'


class CourseView(BaseCourseView, RetrieveAPIViewResponseMixin, generics.RetrieveAPIView):
    serializer_class = CoursesSerializer
    # field = 'name'


class CourseCreateView(BaseCourseView, CreateAPIViewResponseMixin, generics.CreateAPIView):
    serializer_class = CoursesSerializer


class CourseUpdateView(BaseCourseView, UpdateAPIViewResponseMixin, generics.UpdateAPIView):
    serializer_class = CoursesSerializer


class CourseDeleteView(BaseCourseView, DestroyAPIViewResponseMixin, generics.DestroyAPIView):
    pass


