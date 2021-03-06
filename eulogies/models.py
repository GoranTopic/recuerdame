from django.db import models
from django.contrib.auth import get_user_model
from django.urls import include
from memorials.models import Memorial
# Create your models here.


class Eulogy(models.Model):
    # memorial to which it is attached to 
    memorial = models.ForeignKey(Memorial, on_delete=models.CASCADE, related_name='eulogies')

    # user who's wrtting it 
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='eulogy_user')
    # a quote
    quote = models.CharField(max_length=300, null=True, blank=True)
    # an anecdote
    anecdote = models.CharField(max_length=300, null=True, blank=True)
    # writting
    writting = models.CharField(max_length=300, null=True, blank=True)
    # an image
    image = models.ImageField(null=True, blank=True, upload_to='eulogies/')
