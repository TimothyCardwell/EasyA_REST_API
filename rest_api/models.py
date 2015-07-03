from django.db import models
from datetime import datetime

"""
As of 7/3/2015, I have not separated this application into separate apps. For example,
it should be plausible to have an app for users, an app for questions, an app for
answers, an app for tags, etc...

However, since this file is currently only ~100 lines of code, I think splitting them
now is overkill.
"""

# TODO Split these into separate apps?


class Schools(models.Model):
    """ Available universities/colleges """
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']


class Degrees(models.Model):
    """ Available degrees """
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']


class Users(models.Model):
    """ The base User object """
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    username = models.CharField(max_length=20, db_index=True)
    password = models.CharField(max_length=30)
    created = models.DateTimeField(default=datetime.now)
    last_login = models.DateTimeField(default=datetime.now)

    def _get_full_name(self):
        """ Returns the user's full name """
        return '%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)


class UserDetails(Users):
    """ One to One details table for the User object """
    age = models.DateField(null=True)
    school = models.OneToOneField(Schools, null=True)
    degree = models.OneToOneField(Degrees, null=True)
    profession = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True)


class UserRatings(models.Model):
    """ One to Many ratings table for the User object """
    user = models.ForeignKey(Users, related_name='userratings_user')
    rater = models.ForeignKey(Users, related_name='userratings_rater')
    rating = models.IntegerField()
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now, db_index=True)

    class Meta:
        ordering = ['date']


class Tags(models.Model):
    """ Tag object """
    name = models.CharField(max_length=15, unique=True)


class Questions(models.Model):
    """ The base Question object """
    user = models.ForeignKey(Users)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(default=datetime.now, db_index=True)

    class Meta:
        ordering = ['-date']


class QuestionAttachments(models.Model):
    """ One to Many table that defines attachments for the referenced Question """
    question = models.ForeignKey(Questions)
    attachment = models.FileField(upload_to='questions/%Y/%m/%d')
    date = models.DateTimeField(default=datetime.now)


class QuestionTags(models.Model):
    """ This is a Many to Many table for questions and tags. I decided not to define
    this on the Tags object because I don't want that to directly relate to a
    question """
    question = models.ForeignKey(Questions)
    tag = models.ForeignKey(Tags)


class Answers(models.Model):
    """ The base Answers object """
    user = models.ForeignKey(Users)
    question = models.ForeignKey(Questions)
    answer = models.TextField()
    date = models.DateTimeField(default=datetime.now, db_index=True)
    accepted = models.BooleanField()

    class Meta:
        ordering = ['date']


class AnswerAttachments(models.Model):
    """ One to Many table that defines attachments for the referenced Answer """
    answer = models.ForeignKey(Answers)
    attachment = models.FileField(upload_to='answers/%Y/%m/%d')
    date = models.DateTimeField(default=datetime.now)


class Payments(models.Model):
    """ TODO Not certain how this info will be stored. PayPal? Venmo? """
    fake_column = models.CharField(max_length=1)