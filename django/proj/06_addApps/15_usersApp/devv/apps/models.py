from django.db import models
import uuid
from users.models import Profile

class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")

    demo_link = models.CharField(max_length=2000, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)

    tags = models.ManyToManyField("Tag", blank=True) #many to many relationship with tags

    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self): ##this will show project name when you create it in admin
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
        ("up", "Up Vote"),
        ("down", "Down Vote")
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #cascade deletes all the review.
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name