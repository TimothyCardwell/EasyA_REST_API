from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^users/$', views.UsersView.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserView.as_view()),
    url(r'^user-detail/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view()),
    url(r'^schools/$', views.SchoolsView.as_view()),
    url(r'^degrees/$', views.DegreesView.as_view()),
    url(r'^user-ratings/$', views.UserRatingsView.as_view()),
    url(r'^user-rating/(?P<pk>[0-9]+)/$', views.UserRatingView.as_view()),
    url(r'^tags/$', views.TagsView.as_view()),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view()),
    url(r'^questions/$', views.QuestionsView.as_view()),
    url(r'^question/(?P<pk>[0-9]+)/$', views.QuestionView.as_view()),
    url(r'^question-attachments/$', views.QuestionAttachmentsView.as_view()),
    url(r'^question-attachment/(?P<pk>[0-9]+)/$', views.QuestionAttachmentView.as_view()),
    url(r'^question-tags/$', views.QuestionTagsView.as_view()),
    url(r'^question-tag/(?P<pk>[0-9]+)/$', views.QuestionTagView.as_view()),
    url(r'^answers/$', views.AnswersView.as_view()),
    url(r'^answer/(?P<pk>[0-9]+)/$', views.AnswerView.as_view()),
    url(r'^answer-attachments/$', views.AnswerAttachmentsView.as_view()),
    url(r'^answer-attachment/(?P<pk>[0-9]+)/$', views.AnswerAttachmentView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)