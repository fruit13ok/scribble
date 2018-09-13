from django.db import models

# Create your models here.

class Post(models.Model):
    author  = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    
    def __str__(self):
        return self.body

# 1 para, refer to User class object
# 2 para, if user deleted, user's comment will get deleted
# 3 para, user.comments.all allow to see all comment made by that user
#       comments is the name in DB
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author  = models.CharField(max_length=100)
    body  = models.CharField(max_length=100)
    
    def __str__(self):
        return self.body
