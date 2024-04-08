from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(default="Description")
    content = models.TextField()
    
    def __repr__(self):
        return f"Article: {self.title}, from date {self.date}"