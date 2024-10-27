from django.db import models

class Comment1(models.Model):
    post_id = models.IntegerField(null=True, blank=True)
    content = models.TextField()
    writter_uni = models.CharField(max_length=50, null=True, blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"Comment1 on post {self.post_id} by {self.writter_uni}"

class Comment2(models.Model):
    comment1 = models.ForeignKey(Comment1, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField()
    writter_uni = models.CharField(max_length=50, null=True, blank=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"Comment2 by {self.writter_uni} related to Comment1 ID {self.comment1.id}"
