from email.policy import default
from multiprocessing.sharedctypes import Value
from secrets import choice
from tkinter.tix import Tree
from django.db import models
import uuid
from users.models import Profile

class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL) # many to one relationship Profile(parent)--> Project(child)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    feature_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True) #many-to-many relationship Project-->>Tag, remember you do not need to do quotes if the tag model is up here.
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                         primary_key=True, editable=False)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-vote_ratio', '-vote_total', 'title'] # the project with the highest total vote ratio or vote total will be the first on the list.

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True) #query all the review and then all the owner id of that reviews
        return queryset


    @property # run this as an attribute and not as an actual method
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes ) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio

        self.save()


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True) 
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # one-to-many relationship Project(parent)-->Review(child)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                         primary_key=True, editable=False)


    class Meta:
        unique_together = [['owner', 'project' ]] #binding the two tables and make it unique, make sure that nobody tries to cheat and leave a bunch of reviews in the same project.


    
    def __str__(self):
        return self.value


    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                         primary_key=True, editable=False)

    
    def __str__(self):
        return self.name