from django.db import models
from django.urls import reverse, include 
from django.contrib.auth import get_user_model
from memorials.models import Memorial
# Create your models here.

class Tribute(models.Model):
    # memorial this tribute is written for
    memorial = models.ForeignKey(Memorial, on_delete=models.CASCADE, related_name='tributes')
    # user who has written this 
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tribute_user')
    # a quote
    quote = models.TextField(max_length=1000, null=True, blank=True)
    # a quote author
    quote_author = models.CharField(max_length=100, null=True, blank=True)
    # an anecdote
    anecdote = models.TextField(max_length=1000, null=True, blank=True)
    # writting
    writting = models.TextField(max_length=1000, null=True, blank=True)
    # an image
    cover_image = models.ImageField(null=True, blank=True, upload_to='tributes/')
    # creation time
    creation_time = models.DateTimeField(auto_now_add=True, blank=True)
    # likes count 
    likes_count = models.IntegerField(null=True, blank=False)
    # comments count 
    comments_count = models.IntegerField(null=True, blank=False)

    def __str__(self):
        string = ''
        if self.quote != None: 
            string = self.quote
        elif self.anecdote != None:
            string = self.anecdote
        elif self.writting != None:
            string = self.quote
        else:
            string += "by " +  self.user
        return string

    def get_absolute_url(self):
        return reverse('tribute_detail', args=[str(self.pk)])

class Comment(models.Model):
    # Foregn key for the tribute
    tribute = models.ForeignKey(Tribute, on_delete=models.CASCADE, related_name='comments')
    # comment text
    comment = models.TextField(max_length=10000, null=True, blank=False) 
    # author 
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # creation time
    creation_time = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.comment

class Like(models.Model):
    # author 
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # Foregn key for the tribute
    tribute = models.ForeignKey(Tribute, on_delete=models.CASCADE, related_name='likes')



