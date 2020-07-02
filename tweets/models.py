from django.db import models
from django.conf import settings
import random

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    # id = models.AutoField(primary_key=True)
    # blank=True -> not required in django
    # null=True -> not required in database
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    # foreign key -> many users can have many tweets
    # if owner is deleted, all their tweets are deleted
    # if want tweets to stay, set (User, null=True, on_delete=models.set_NULL) 
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    
    # This will display tweet contents instead of tweet number #
    # def __str__(self):
    #     return self.content
    

    def serialize(self):
        return {
            "id": self.id, 
            "content": self.content,
            "likes": random.randint(0, 100)
        }