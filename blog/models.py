from django.db import models
from django.contrib.auth.models import  User

# Create your models here.

class PostModel(models.Model):
    title= models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    publication_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ("-publication_date",)

    def __str__(self):
        return self.title

    # count he comment
    def comment_count(self):
        return self.comment_set.all().count()

    # getting all count and pass to templates
    def comments(self):
        return self.comment_set.all()

    
class comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content=models.CharField(max_length=500)

    def __str__(self):
        return self.content
