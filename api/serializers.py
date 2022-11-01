
from .models import *
from rest_framework import serializers

class ArticleSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField(method_name='get_image_url')
    class Meta:
        model = Articles
        fields = ['id', 'name', 'content', 'avtor', 'src', 'file']

        # def get_image_url(self, obj):
        #     request = self.context.get('request')
        #     image_url = obj.image.url
        #     return request.build_absolute_uri(image_url)

class BookSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField(method_name='get_image_url')
    class Meta:
        model = Books
        fields = ['id', 'name', 'content', 'avtor', 'date', 'src', 'file']

        # def get_image_url(self, obj):
        #     request = self.context.get('request')
        #     image_url = obj.image.url
        #     return request.build_absolute_uri(image_url)

class DocumentSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField(method_name='get_image_url')
    class Meta:
        model = Documents
        fields = ['id', 'name', 'content', 'avtor', 'date', 'src', 'file']

        # def get_image_url(self, obj):
        #     request = self.context.get('request')
        #     image_url = obj.image.url
        #     return request.build_absolute_uri(image_url)

class EventSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField(method_name='get_image_url')
    class Meta:
        model = Events
        fields = ['id', 'name', 'content', 'avtor', 'date','src', 'file']

        # def get_image_url(self, obj):
        #     request = self.context.get('request')
        #     image_url = obj.image.url
        #     return request.build_absolute_uri(image_url)

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'name', 'content', 'avtor', 'date','src', 'file']

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'name', 'content', 'avtor', 'date','src', 'file']

class VideoSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField(method_name='get_image_url')
    class Meta:
        model = Videos
        fields = ['id', 'name',  'avtor', 'date', 'file']

        # def get_image_url(self, obj):
        #     request = self.context.get('request')
        #     image_url = obj.image.url
        #     return request.build_absolute_uri(image_url)


class GroupUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GroupUser
        fields = ['id', 'user_id', 'group_id' ]
        depth = 1

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'chat', 'avtor', 'file']

class SmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sms
        fields = ['text', 'group', 'date', 'user', 'fio']
        # depth = 1


