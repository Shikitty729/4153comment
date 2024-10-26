from django.db import models

class Comment1(models.Model):
    post_id = models.IntegerField(null=True, blank=True)
    content = models.TextField()
    writter_uni = models.CharField(max_length=50, null=True, blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'Comment1: {self.content[:20]}'

class Comment2(models.Model):
    comment1 = models.ForeignKey(Comment1, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField()
    writter_uni = models.CharField(max_length=50, null=True, blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'Comment2: {self.content[:20]}'
