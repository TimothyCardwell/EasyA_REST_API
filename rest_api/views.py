from rest_api.models import *
from rest_api.serializers import *
from rest_framework import generics


class UsersView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailSerializer


class SchoolsView(generics.ListAPIView):
    queryset = Schools.objects.all()
    serializer_class = SchoolSerializer


class DegreesView(generics.ListAPIView):
    queryset = Degrees.objects.all()
    serializer_class = DegreeSerializer


class UserRatingsView(generics.ListAPIView):
    queryset = UserRatings.objects.all()
    serializer_class = UserRatingSerializer


class UserRatingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserRatings.objects.all()
    serializer_class = UserRatingSerializer


class TagsView(generics.ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer


class TagView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer


class QuestionsView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer


class QuestionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer


class QuestionAttachmentsView(generics.ListAPIView):
    queryset = QuestionAttachments.objects.all()
    serializer_class = QuestionAttachmentSerializer


class QuestionAttachmentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionAttachments.objects.all()
    serializer_class = QuestionAttachmentSerializer


class QuestionTagsView(generics.ListAPIView):
    queryset = QuestionTags.objects.all()
    serializer_class = QuestionTagSerializer


class QuestionTagView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionTags.objects.all()
    serializer_class = QuestionTagSerializer


class AnswersView(generics.ListAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer


class AnswerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answers.objects.all()
    serializer_class = AnswerSerializer


class AnswerAttachmentsView(generics.ListAPIView):
    queryset = AnswerAttachments.objects.all()
    serializer_class = AnswerAttachmentSerializer


class AnswerAttachmentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnswerAttachments.objects.all()
    serializer_class = AnswerAttachmentSerializer