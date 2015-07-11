from rest_framework import serializers
from rest_api.models import *

"""
http://www.django-rest-framework.org/api-guide/serializers/#inspecting-a-modelserializer
To exclude fields, use exclude

"""


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degrees


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails


class UserRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRatings


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions


class QuestionAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAttachments


class QuestionTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionTags


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers


class AnswerAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerAttachments


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments